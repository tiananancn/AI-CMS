# Design: CMS中英双语切换功能

## Architecture Overview

采用**混合国际化方案**结合Flask-Babel框架和自定义翻译映射：

```
┌─────────────────────────────────────────┐
│           User Request                  │
│  (URL/导航栏/Accept-Language Header)    │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│         Language Detection              │
│  1. URL Parameter (?lang=en)           │
│  2. Session Storage                     │
│  3. Accept-Language Header              │
│  4. Default (zh_CN)                     │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│         Translation Layer               │
│  ┌──────────────┐  ┌─────────────────┐ │
│  │ Static Text  │  │ Dynamic Content │ │
│  │ (Templates)  │  │ (Database)      │ │
│  │ {% trans %}  │  │ Translation     │ │
│  └──────────────┘  │ Maps            │ │
│                    └─────────────────┘ │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│         Rendered Page                   │
│  - HTML lang attribute                  │
│  - Translated content                   │
│  - Language switcher UI                 │
└─────────────────────────────────────────┘
```

## Component Design

### 1. Flask-Babel Configuration
**Location**: `app.py`
```python
# 语言检测函数
def get_locale():
    # 优先级：URL > Session > Header > Default
    pass

# Babel初始化
babel = Babel(app, locale_selector=get_locale)

# 上下文处理器
@app.context_processor
def inject_translations():
    return dict(__=gettext, LANGUAGES=LANGUAGES, current_lang=get_locale())
```

**Rationale**:
- 使用标准的Flask-Babel国际化框架
- 上下文处理器自动注入翻译函数和语言变量到所有模板

### 2. Static Text Translation (Templates)
**Files**: `templates/base.html`, `templates/index.html`, `templates/admin/base.html`
```html
<!-- 使用{% trans %}标记可翻译文本 -->
<h1>{% trans %}欢迎来到AI-CMS{% endtrans %}</h1>

<!-- 动态变量不能放在{% trans %}中 -->
<p>{{ user_name }}</p>
```

**Rationale**:
- 模板中的硬编码文本使用Babel的`{% trans %}`标记
- 变量内容不翻译（避免复杂性和性能问题）
- 通过pybabel工具自动提取翻译

### 3. Dynamic Content Translation (Database)
**Location**: `app.py` - 翻译映射字典
```python
MENU_TRANSLATIONS = {
    'zh_CN': {'首页': '首页', '文章': '文章'},
    'en': {'首页': 'Home', '文章': 'Articles'}
}

HOMEPAGE_CONFIG_TRANSLATIONS = {
    'zh_CN': {'欢迎来到AI-CMS': '欢迎来到AI-CMS'},
    'en': {'欢迎来到AI-CMS': 'Welcome to AI-CMS'}
}
```

**Rationale**:
- 数据库中的动态内容（如菜单项、配置）通过翻译映射处理
- 避免修改数据模型结构
- 简单直接，易于理解和维护

### 4. Language Switching Mechanism
**Route**: `/set_language/<lang>`
```python
@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in LANGUAGES:
        session['lang'] = lang  # 保存到Session
        referrer = request.referrer or url_for('index')
        return redirect(referrer)  # 返回上一页
```

**Rationale**:
- 使用Session保持语言偏好
- 自动重定向到上一页提供良好用户体验
- 支持书签和直接访问特定页面

### 5. Translation Files
**Files**: `translations/*.po`, `translations/*.mo`
- `.po`文件：人类可编辑的翻译文本
- `.mo`文件：编译后的二进制格式，供应用读取

**Rationale**:
- 使用标准的GNU gettext格式
- 支持翻译工具和协作
- 编译后的.mo文件提供高性能查找

## Trade-offs and Decisions

### Decision 1: Static vs Dynamic Translation
**Choice**: 混合方案
- **Pro**: 静态文本用Babel（成熟工具），动态内容用映射字典（简单直接）
- **Con**: 需要维护两套翻译机制

**Alternative Considered**: 全部用翻译映射
- **Rejected**: 失去Babel工具链优势，翻译维护困难

### Decision 2: Translation Scope
**Choice**: 只翻译界面文本，不翻译用户内容
- **Pro**: 简单，避免复杂的内容管理
- **Con**: 用户创建的内容（如文章标题）仍为中文

**Alternative Considered**: 翻译所有用户内容
- **Rejected**: 复杂度过高，超出当前需求

### Decision 3: Language Persistence
**Choice**: Session存储
- **Pro**: 简单，无服务器端存储负担
- **Con**: 新浏览器会话需要重新设置

**Alternative Considered**: 用户表存储语言偏好
- **Rejected**: 需要用户认证系统，超出当前需求

## Performance Considerations

1. **翻译文件加载**: .mo文件在应用启动时加载一次，内存中缓存
2. **翻译映射**: 字典查找O(1)时间复杂度
3. **Session开销**: 每个请求读取session['lang']，开销极小

## Extensibility

### Adding New Languages
1. 在`LANGUAGES`字典中添加语言代码
2. 创建对应的翻译文件目录
3. 添加翻译映射（如果需要）
4. 重新编译翻译文件

### Adding New Translatable Content
1. 静态文本：在模板中添加`{% trans %}`标记
2. 动态文本：在相应映射字典中添加键值对
3. 重新提取和编译翻译

## Security Considerations

1. **XSS**: 翻译文本在渲染前经过Jinja2转义
2. **Session安全**: 使用Flask的安全session机制
3. **语言代码验证**: 只允许预定义的语言代码

## Testing Strategy

1. **单元测试**: 验证翻译函数和映射字典
2. **集成测试**: 验证页面渲染的语言正确性
3. **端到端测试**: 验证用户切换语言的完整流程

## Monitoring and Debugging

1. **语言检测日志**: 记录语言选择的优先级路径
2. **缺失翻译**: 监控未翻译的文本（msgstr为空）
3. **性能监控**: 监控翻译查找的性能影响
