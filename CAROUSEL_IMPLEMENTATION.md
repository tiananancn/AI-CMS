# 轮播图管理功能实现说明

## 功能概述

为CMS系统添加了首页轮播图管理功能，管理员可以在后台自定义配置首页轮播图，支持从图库选择或直接上传新图片，支持拖拽排序。

## 主要功能

1. **轮播图管理页面** (`/admin/carousel-management`)
   - 显示当前配置的轮播图列表
   - 支持拖拽排序调整显示顺序
   - 可从图库选择图片添加
   - 支持直接上传新图片
   - 可删除不需要的轮播图

2. **API接口**
   - `GET /api/admin/carousel-config` - 获取轮播图配置
   - `PUT /api/admin/carousel-config` - 更新轮播图配置

3. **首页显示**
   - 最多显示5张轮播图
   - 按配置顺序显示
   - 自动适应不同屏幕尺寸

## 修改文件

### 1. app.py

**修改首页路由** (第395-407行)
```python
# 获取轮播图片（从配置中读取）
carousel_image_ids = config_data.get('carousel_images', [])
if carousel_image_ids:
    # 根据ID获取轮播图片
    carousel_images = Image.query.filter(
        Image.id.in_(carousel_image_ids),
        Image.status=='published'
    ).all()
    # 按配置顺序排序
    data['carousel_images'] = sorted(carousel_images, key=lambda x: carousel_image_ids.index(x.id) if x.id in carousel_image_ids else 999)
else:
    # 如果没有配置，使用最新5张图片作为默认
    data['carousel_images'] = Image.query.filter_by(status='published').order_by(Image.created_at.desc()).limit(5).all()
```

**添加轮播图管理路由和API** (第1016-1075行)
- `/admin/carousel-management` - 轮播图管理页面
- `/api/admin/carousel-config` (GET) - 获取轮播图配置
- `/api/admin/carousel-config` (PUT) - 更新轮播图配置

### 2. 创建轮播图管理模板

**templates/admin/carousel_management.html**
- 响应式设计，支持拖拽排序
- 集成图片库选择器
- 支持文件上传
- 实时预览和编辑

### 3. 修改导航菜单

**templates/admin/base.html** (第242行和第255-259行)
- 在"版面管理"子菜单中添加"轮播图管理"链接
- 更新子菜单展开逻辑

## 使用说明

### 访问轮播图管理

1. 登录后台管理系统
2. 在侧边栏中点击"版面管理" → "轮播图管理"

### 配置轮播图

1. **从图库选择**
   - 点击"从图片库选择"按钮
   - 在弹窗中选择要添加的图片（支持多选）
   - 点击"添加选中图片"

2. **上传新图片**
   - 点击"上传新图片"按钮
   - 选择图片文件（支持多选）
   - 图片将自动添加到轮播图列表

3. **调整顺序**
   - 拖拽轮播图列表中的拖拽手柄（6个点图标）
   - 松开鼠标完成排序

4. **删除图片**
   - 点击轮播图右侧的删除按钮（×）

5. **保存配置**
   - 完成编辑后点击"保存更改"按钮

### 首页展示

- 轮播图会在首页顶部自动轮播显示
- 支持触摸滑动和键盘导航
- 响应式设计，自动适应各种屏幕尺寸

## 技术特点

1. **拖拽排序**: 使用 SortableJS 库实现流畅的拖拽体验
2. **实时预览**: 管理员可以实时看到配置效果
3. **文件上传**: 支持多文件同时上传
4. **图片库集成**: 与现有图片管理系统无缝集成
5. **响应式设计**: 支持移动端和平板设备

## 配置限制

- 最多配置5张轮播图
- 图片格式支持：JPG、PNG、GIF、WebP
- 建议图片尺寸：1920×800 像素
- 单个文件大小限制：10MB

## 后续优化建议

1. **图片压缩**: 添加图片自动压缩功能
2. **批量操作**: 支持批量上传和删除
3. **预览模式**: 在管理页面添加轮播预览
4. **动画效果**: 添加更多轮播动画选项
5. **链接配置**: 为每张轮播图配置跳转链接
6. **文字覆盖**: 支持在轮播图上添加文字标题和描述
