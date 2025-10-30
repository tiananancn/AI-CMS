# CMS多语言功能说明

## 功能概述

CMS系统已成功增加中英文切换功能，用户可以在中文和英文之间自由切换，提供更好的用户体验。

## 支持的语言

- **中文（简体）** - zh_CN（默认语言）
- **英文（美国）** - en_US

## 语言切换方式

### 1. 导航栏语言切换器
- 点击导航栏右侧的地球图标
- 从下拉菜单选择所需语言（🇨🇳 中文 或 🇬🇧 English）
- 选择后立即生效，页面刷新后保持所选语言

### 2. URL参数切换
- 英文：http://localhost:8080/set_language/en
- 中文：http://localhost:8080/set_language/zh_CN
- 切换后会重定向回上一页

### 3. 浏览器语言偏好
- 系统会自动检测浏览器语言设置
- 优先级：用户选择 > session > 浏览器设置 > 默认中文

## 技术实现

### 已添加的依赖
```
Flask-Babel==4.0.0
```

### 核心文件

1. **app.py** - 后端国际化支持
   - 配置Babel国际化
   - 语言选择器函数
   - 语言切换路由

2. **templates/base.html** - 前端模板
   - 添加语言切换器UI
   - 使用{% trans %}标签标记翻译文本

3. **babel.cfg** - 翻译配置文件
   - 指定需要提取翻译的文件

4. **translations/** - 翻译文件目录
   - `zh_CN/LC_MESSAGES/` - 中文翻译
   - `en_US/LC_MESSAGES/` - 英文翻译
   - `messages.pot` - 翻译模板文件

### 翻译管理命令

```bash
# 提取翻译文本
pybabel extract -F babel.cfg -o messages.pot .

# 初始化新语言
pybabel init -i messages.pot -d translations -l <语言代码>

# 编译翻译文件
pybabel compile -d translations

# 更新翻译（添加新文本后）
pybabel update -i messages.pot -d translations
```

## 已翻译的文本

目前已翻译的文本包括：
- 管理后台 / Admin Panel
- 关于CMS / About CMS
- 这是一个功能完整的内容管理系统，支持文章、视频和图片管理。/ This is a fully functional content management system supporting articles, videos, and image management.
- 联系我们 / Contact Us
- 保留所有权利 / All rights reserved

## 扩展翻译

### 添加新翻译文本

1. **在Python代码中**：
```python
from flask_babel import gettext
# 使用翻译函数
message = gettext("需要翻译的文本")
```

2. **在模板中**：
```html
<!-- 简单文本 -->
{% trans %}需要翻译的文本{% endtrans %}

<!-- 带变量的文本 -->
{% trans %}Hello {{ name }}{% endtrans %}
```

3. **提取和编译**：
```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel compile -d translations
```

### 翻译文件位置

- 中文：`translations/zh_CN/LC_MESSAGES/messages.po`
- 英文：`translations/en_US/LC_MESSAGES/messages.po`

编辑.po文件，在msgstr中添加翻译内容，然后重新编译。

## 使用示例

### 添加更多导航栏翻译

例如，修改templates中的菜单项：
```html
<!-- 修改前 -->
<a class="nav-link">首页</a>

<!-- 修改后 -->
<a class="nav-link">{% trans %}首页{% endtrans %}</a>
```

然后提取翻译并添加中文/英文翻译即可。

## 注意事项

1. 翻译文件修改后需要重新编译：`pybabel compile -d translations`
2. 开发环境下修改翻译文件需要重启应用生效
3. 生产环境应使用.wsgi服务器而非开发服务器
4. 建议使用Git管理翻译文件，.po和.mo文件都应提交

## 浏览器兼容性

支持所有现代浏览器：
- Chrome/Edge (Chromium)
- Firefox
- Safari
- Opera

## 性能影响

- 翻译文件加载影响极小（.mo文件已编译）
- 内存占用：每种语言约几KB
- 推荐在生产环境中启用缓存

## 下一步计划

1. 添加更多文本的翻译
2. 支持更多语言（如繁体中文、日语、韩语）
3. 添加语言切换的动画效果
4. 自动检测并建议用户语言

## 测试

测试语言切换功能：
```bash
# 启动应用
python app.py

# 访问首页（默认中文）
curl http://localhost:8080/

# 切换到英文
curl http://localhost:8080/set_language/en

# 验证英文显示
curl -b session信息 http://localhost:8080/
```
