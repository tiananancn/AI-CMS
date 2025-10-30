# 语言切换功能修复说明

## 问题描述
中英语言切换后，首页和后台没有变成英语，页面内容仍然是中文。

## 问题原因
1. 模板中的大部分文本没有用 `{% trans %}` 标签标记为可翻译
2. 翻译文件（.po）中的 msgstr 字段为空，没有提供英文翻译
3. 部分模板语法错误（{% trans %} 标签中不能包含变量）
4. 后台路由没有正确传递语言相关变量

## 修复内容

### 1. 模板国际化标记
- **base.html**: 标记了标题、菜单项、页脚等文本
- **index.html**: 标记了首页所有可见文本（欢迎信息、按钮、标题等）
- **admin/base.html**: 标记了后台管理界面所有文本

### 2. 翻译文件生成和更新
```bash
# 提取翻译文本
pybabel extract -F babel.cfg -o messages.pot .

# 更新翻译文件
pybabel update -i messages.pot -d translations -l zh_CN
pybabel update -i messages.pot -d translations -l en_US

# 编译翻译文件
pybabel compile -d translations
```

### 3. 英文翻译补充
为所有标记的文本提供了完整的英文翻译，包括：
- 首页：标题、按钮、提示信息等
- 后台：菜单、标题、按钮、表单标签等
- 通用：版权信息、导航等

### 4. 修复模板语法
- 移除了 `{% trans %}{{ variable }}{% endtrans %}` 这种错误用法
- 变量文本直接在模板中显示，不进行翻译
- 只有静态文本才使用 `{% trans %}` 标记

### 5. 添加上下文处理器
在 app.py 中添加了：
```python
@app.context_processor
def inject_translations():
    return dict(__=gettext, LANGUAGES=LANGUAGES, current_lang=get_locale())

@app.before_request
def add_language_vars():
    g.current_lang = get_locale()
    g.LANGUAGES = LANGUAGES
```

## 测试结果

### ✅ 前台页面语言切换
**英文页面**:
- `<html lang="en">`
- 标题：`AI-CMS - Intelligent Content Management System`
- 欢迎信息：`Welcome to AI-CMS`
- 按钮：`Read Articles`, `Watch Videos`, `View More`
- 区域标题：`Latest Articles`, `Latest Videos`, `Latest Images`

**中文页面**:
- `<html lang="zh_CN">`
- 标题：`AI-CMS - 智能内容管理系统`
- 欢迎信息：`欢迎来到AI-CMS`
- 按钮：`阅读文章`, `观看视频`, `查看更多`
- 区域标题：`最新文章`, `最新视频`, `最新图片`

### ✅ 语言切换功能
- 访问 `/set_language/en` → 切换到英文
- 访问 `/set_language/zh_CN` → 切换到中文
- 语言偏好保存在 session 中
- 支持浏览器 Accept-Language 头自动选择语言

### ✅ 后台管理页面
- HTML lang 属性动态设置
- 菜单和界面文本支持翻译
- 登录页面文本支持翻译

## 使用方法

### 切换语言
1. **通过URL**：
   - 英文：http://localhost:8080/set_language/en
   - 中文：http://localhost:8080/set_language/zh_CN

2. **通过导航栏**：
   - 点击右上角语言切换下拉菜单
   - 选择 English 或 中文

3. **通过浏览器设置**：
   - 浏览器发送 Accept-Language 头
   - 应用自动选择对应语言

### 添加新翻译
1. 在模板中使用 `{% trans %}文本{% endtrans %}` 标记
2. 重新提取翻译：`pybabel extract -F babel.cfg -o messages.pot .`
3. 更新翻译文件：`pybabel update -i messages.pot -d translations -l en_US`
4. 编辑 `translations/en_US/LC_MESSAGES/messages.po`，添加 msgstr
5. 重新编译：`pybabel compile -d translations`

## 技术要点

1. **Babel国际化框架**：使用 Flask-Babel 进行国际化处理
2. **模板标记**：`{% trans %}` 标签标记可翻译文本
3. **语言检测**：优先级为 用户选择 > session > 请求头 > 默认
4. **变量处理**：动态内容（数据库、配置）不翻译，只翻译静态文本
5. **会话保持**：语言偏好保存在 Flask session 中

## 文件变更

- `templates/base.html` - 添加翻译标记
- `templates/index.html` - 添加翻译标记
- `templates/admin/base.html` - 添加翻译标记，修复HTML lang属性
- `translations/en_US/LC_MESSAGES/messages.po` - 添加英文翻译
- `app.py` - 添加上下文处理器和语言变量注入
