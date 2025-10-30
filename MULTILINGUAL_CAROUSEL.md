# 轮播图管理功能多语言支持

## 更新说明

已完成轮播图管理功能的中英文国际化支持，所有新增的文本都已添加翻译。

## 新增翻译条目

### 轮播图管理页面翻译

1. **轮播图管理** / Carousel Management
2. **首页轮播图管理** / Homepage Carousel Management
3. **保存更改** / Save Changes
4. **最多可配置5张轮播图。拖拽图片可以调整显示顺序。** / You can configure up to 5 carousel images. Drag images to adjust display order.
5. **当前轮播图** / Current Carousel Images
6. **还没有配置轮播图** / No carousel images configured yet
7. **添加轮播图** / Add Carousel Images
8. **从图片库选择** / Select from Image Library
9. **上传新图片** / Upload New Images
10. **建议尺寸：1920×800 像素** / Recommended size: 1920×800 pixels
11. **支持格式：JPG、PNG、GIF、WebP** / Supported formats: JPG, PNG, GIF, WebP
12. **图片库** / Image Library
13. **搜索图片...** / Search images...
14. **选择轮播图** / Select Carousel Images
15. **取消** / Cancel
16. **添加选中图片** / Add Selected Images
17. **最多只能添加5张轮播图！** / You can only add up to 5 carousel images!
18. **文件** / File
19. **超过10MB限制！** / exceeds 10MB limit!
20. **上传失败！** / Upload failed!
21. **上传** / Upload
22. **失败:** / failed:
23. **出错:** / error:
24. **轮播图配置已保存！** / Carousel configuration saved!
25. **保存失败，请重试！** / Save failed, please try again!
26. **保存出错，请重试！** / Error saving, please try again!

## 文件修改

### 1. 模板文件 (templates/admin/carousel_management.html)

将所有硬编码的中文文本替换为 `{% trans %}` 标签：

```html
<!-- 修改前 -->
<h4>轮播图管理</h4>

<!-- 修改后 -->
<h4>{% trans %}轮播图管理{% endtrans %}</h4>
```

JavaScript 代码中的提示信息也使用 `{% trans %}` 标签：

```javascript
// 修改前
alert('最多只能添加5张轮播图！');

// 修改后
alert('{% trans "最多只能添加5张轮播图！" %}');
```

### 2. 翻译文件

使用 Babel 提取和编译翻译：

```bash
# 提取翻译文本
pybabel extract -F babel.cfg -o messages.pot .

# 更新英文翻译
pybabel update -i messages.pot -d translations -l en_US

# 更新中文翻译
pybabel update -i messages.pot -d translations -l zh_CN

# 编译翻译文件
pybabel compile -d translations
```

## 测试结果

### 中文界面
- ✅ 所有文本正确显示中文
- ✅ 语言切换正常

### 英文界面
- ✅ 轮播图管理 → Carousel Management
- ✅ 首页轮播图管理 → Homepage Carousel Management
- ✅ 保存更改 → Save Changes
- ✅ 所有新增功能正确翻译

## 语言切换

用户可以通过以下方式切换语言：

1. **URL 参数**: `/set_language/en` 或 `/set_language/zh_CN`
2. **后台管理界面**: 点击右上角语言切换器
3. **Session 持久化**: 语言设置保存在 Session 中

## 技术实现

### 翻译标记

在 Jinja2 模板中使用 `{% trans %}` 标记需要翻译的文本：

```html
{% trans %}文本内容{% endtrans %}
```

在 JavaScript 中也可以使用（需要是静态文本）：

```javascript
alert('{% trans "需要翻译的文本" %}');
```

### 动态文本翻译

对于运行时生成的文本，在 Python 端使用 `gettext()` 函数：

```python
from flask_babel import gettext

message = gettext('欢迎使用CMS')
```

### 翻译文件结构

```
translations/
├── en_US/
│   └── LC_MESSAGES/
│       ├── messages.po  # 英文翻译源文件
│       └── messages.mo  # 编译后的英文翻译文件
└── zh_CN/
    └── LC_MESSAGES/
        ├── messages.po  # 中文翻译源文件
        └── messages.mo  # 编译后的中文翻译文件
```

## 注意事项

1. **重新生成翻译**: 修改模板后需要重新提取和编译翻译
2. **fuzzy 标记**: 翻译文件中的 `# fuzzy` 标记表示需要人工校对
3. **静态文本**: JavaScript 中的翻译文本必须是静态的，不能包含变量
4. **浏览器缓存**: 切换语言后可能需要清除浏览器缓存

## 下一步计划

1. 添加更多语言的翻译支持
2. 完善轮播图功能的英文提示信息
3. 优化移动端的语言切换体验
4. 添加语言检测和自动切换功能
