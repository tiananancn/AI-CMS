# 首页内容管理功能说明

## 功能概述

新增了首页内容管理功能，允许管理员在后台选择特定的文章、图片、视频和链接在首页显示。只有选择的内容才会在首页显示，未选择的内容不会在首页出现。

## 主要功能

### 1. 首页内容管理页面

**访问路径**: 后台管理 → 版面管理 → 首页内容管理

**页面功能**:
- **文章区域管理**: 选择要显示在首页的文章
- **视频区域管理**: 选择要显示在首页的视频
- **图片区域管理**: 选择要显示在首页的图片
- **链接区域管理**: 选择要显示在首页的链接

### 2. 页面特性

1. **搜索功能**
   - 每个区域都有搜索框
   - 支持实时过滤内容列表

2. **拖拽排序**
   - 可以拖拽调整已选择内容的显示顺序
   - 顺序决定了在首页的显示顺序

3. **添加/移除内容**
   - 点击"+"按钮添加内容
   - 点击"×"按钮移除内容
   - 实时更新列表

4. **保存配置**
   - 点击"保存配置"按钮保存所有更改
   - 配置会立即生效

## 技术实现

### 1. 数据结构

在 `HomepageConfig` 的 `sections` 中新增了 `selected_ids` 字段：

```json
{
  "sections": [
    {
      "type": "articles",
      "visible": true,
      "order": 1,
      "title": "最新文章",
      "limit": 6,
      "selected_ids": [1, 2, 3]  // 选中的文章ID列表
    },
    ...
  ]
}
```

### 2. 首页路由逻辑

修改了首页路由 (`app.py:409-463`)，支持根据配置显示选定的内容：

```python
# 获取配置的内容ID列表
selected_ids = section.get('selected_ids', [])

if section_type == 'articles':
    if selected_ids:
        # 如果配置了特定文章ID，按配置顺序显示
        articles = Article.query.filter(
            Article.id.in_(selected_ids),
            Article.status=='published'
        ).all()
        data['articles'] = sorted(articles, key=lambda x: selected_ids.index(x.id) if x.id in selected_ids else 999)
    else:
        # 否则显示最新的文章
        data['articles'] = Article.query.filter_by(status='published').order_by(Article.created_at.desc()).limit(limit).all()
```

### 3. 配置文件

- **模板文件**: `templates/admin/homepage_content.html`
- **路由**: `/admin/homepage-content` (GET)
- **菜单导航**: 已添加到"版面管理"子菜单中

### 4. 初始化逻辑

在 `init_homepage_config()` 函数中：

1. **新配置**: 自动添加 `selected_ids: []` 字段
2. **现有配置**: 检查并补充缺失的 `selected_ids` 字段

## 使用说明

### 配置首页内容

1. **访问页面**
   - 登录后台管理系统
   - 进入"版面管理" → "首页内容管理"

2. **选择文章**
   - 在左侧搜索框输入关键词过滤文章
   - 点击文章右侧的"+"按钮添加到右侧列表
   - 拖拽调整显示顺序
   - 点击"×"按钮移除

3. **选择视频/图片/链接**
   - 操作步骤同文章选择

4. **保存配置**
   - 完成所有选择后，点击"保存配置"按钮
   - 提示"首页内容配置已保存！"即表示成功

### 查看效果

访问前台首页 (http://localhost:8080/)，查看配置的效果：

- 首页只会显示已选择的内容
- 显示顺序与配置顺序一致
- 如果某个区域没有选择任何内容，该区域不会显示

## 配置示例

### 示例1: 只显示指定文章

```json
{
  "type": "articles",
  "visible": true,
  "order": 1,
  "title": "推荐文章",
  "limit": 6,
  "selected_ids": [1, 5, 9]
}
```

首页将只显示ID为1、5、9的三篇文章，顺序为：文章1 → 文章5 → 文章9。

### 示例2: 不显示文章区域

如果 `selected_ids` 为空数组，首页将显示最新的6篇文章。

如果不想显示文章区域，可以将 `visible` 设置为 `false`。

## 多语言支持

已为所有新增文本添加了多语言支持：

- **首页内容管理** / Homepage Content Management
- **文章区域** / Articles Section
- **视频区域** / Videos Section
- **图片区域** / Images Section
- **链接区域** / Links Section
- **选择要显示的...** / Select ... to display
- **已选择的...** / Selected ...
- **搜索...** / Search ...
- **保存配置** / Save Configuration

## 注意事项

1. **内容状态**: 只有状态为 `published` 的内容才能在首页显示
2. **显示限制**: 每个区域显示的内容数量受 `limit` 字段限制
3. **排序规则**: 按 `selected_ids` 数组中的顺序显示，未选择的内容不会显示
4. **兼容性**: 如果没有配置 `selected_ids`，会自动显示最新内容（向后兼容）

## 相关文件

### 修改的文件

1. **app.py**
   - `index()`: 首页路由逻辑 (第409-463行)
   - `admin_homepage_content()`: 首页内容管理页面路由 (第1107-1112行)
   - `init_homepage_config()`: 初始化函数 (第126-192行)

2. **templates/admin/base.html**
   - 添加导航菜单项 (第255-259行)
   - 更新子菜单展开条件 (第242行)

### 新增的文件

1. **templates/admin/homepage_content.html**: 首页内容管理页面模板

## 测试建议

1. **测试选择功能**: 选择不同的文章、图片、视频和链接
2. **测试排序功能**: 拖拽调整显示顺序
3. **测试搜索功能**: 输入关键词过滤内容
4. **测试保存功能**: 保存配置并检查前台首页
5. **测试多语言**: 切换语言查看翻译效果

## 后续优化建议

1. **批量选择**: 添加"全选/反选"功能
2. **分类过滤**: 按分类筛选内容
3. **预览功能**: 在管理页面预览首页效果
4. **配置导入/导出**: 支持配置的备份和恢复
