# AI-CMS 智能内容管理系统 🎯

[![English](https://img.shields.io/badge/Language-English-blue.svg)](README.md)
[![中文](https://img.shields.io/badge/语言-中文-red.svg)](README_zh.md)
[![Python](https://img.shields.io/badge/Python-3.7+-green.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

基于 Flask 构建的轻量级但功能强大的内容管理系统（CMS），具备文章、视频和图片管理功能，拥有美观的admin界面和灵活的前台展示，支持高级拖拽式页面编辑器、库集成和单元格合并功能。

## ✨ 功能特性

### 🎨 前台功能
- **首页展示**: 显示最新的文章、视频、图片和链接
- **内容可配置**: 可选择特定内容在首页显示
- **文章系统**:
  - 文章列表（分页和分类筛选）
  - 文章详情页（富文本内容）
  - 分类和标签系统
  - 封面图支持
- **视频系统**:
  - 视频列表（分页和分类筛选）
  - 视频详情页（本地文件和外部链接）
  - 分类和标签系统
- **图片系统**:
  - 网格画廊展示
  - 图片详情页
  - 图片下载功能
  - 模态框预览
- **链接区域**: 美观的链接卡片展示（图标或自定义图片）

### 🛠️ 管理后台
- **仪表盘**: 系统统计信息显示
- **文章管理**:
  - 创建、编辑、删除文章
  - 富文本编辑器（Quill.js）
  - 文章状态管理（已发布/草稿）
  - 分类和标签管理
  - 封面图选择器
- **视频管理**:
  - 添加、编辑、删除视频
  - 支持本地视频文件和外部链接（YouTube、Bilibili等）
  - 视频状态管理
  - 分类和标签管理
- **图片管理**:
  - 图片上传功能
  - 图片预览
  - 图片信息显示
  - 分类和标签管理
- **链接管理**:
  - 添加、编辑、删除链接
  - 支持 Font Awesome 图标或自定义图片
  - 链接分类和描述
  - 拖拽排序
  - 显示/隐藏控制
- **菜单管理**: 动态导航菜单，支持拖拽排序
- **首页配置**: 可自定义首页布局
- **首页内容管理**: 选择并排列特定内容在首页显示
- **轮播图管理**: 管理首页横幅图片，支持拖拽排序
- **动态页面**: 高级拖拽式页面编辑器，支持：
  - **网格布局编辑器**: 可视化网格页面构建器
  - **9种元素类型**: 文本、图片、视频、引用、按钮、分隔线、相册、图标、卡片
  - **库集成**: 直接从现有库选择内容
    - 从图片库选择图片
    - 从视频库选择视频
    - 从图库选择多张图片创建相册
    - 在文本元素中引用文章
  - **单元格合并**: 合并和取消合并网格单元格，实现灵活布局
    - 多选单元格（Ctrl/Cmd + 点击）
    - 将单元格合并为更大区域
    - 视觉反馈和尺寸标识
    - 自动数据持久化
- **多语言支持**: 内置中英文切换功能

### 🌍 多语言支持
- **内置语言切换**: 中英文自由切换
- **自动检测**: 自动识别浏览器语言偏好
- **会话持久化**: 保存用户语言偏好
- **翻译管理**: 基于 Flask-Babel 的翻译系统

### 📊 RESTful API
完整的 RESTful API 接口：
- `GET /api/articles` - 获取所有文章
- `GET /api/articles/<slug>` - 获取特定文章
- `GET /api/videos` - 获取所有视频
- `GET /api/videos/<slug>` - 获取特定视频
- `GET /api/images` - 获取所有图片
- `GET /api/images/<slug>` - 获取特定图片
- `GET /api/links` - 获取可见链接（前台）
- `GET /api/admin/links` - 获取所有链接（管理）
- `POST /api/admin/links` - 创建新链接
- `PUT /api/admin/links/<id>` - 更新链接
- `DELETE /api/admin/links/<id>` - 删除链接
- `POST /api/admin/links/reorder` - 重新排序链接
- `GET /api/menu-items` - 获取菜单项
- `GET /api/admin/menu-items` - 获取所有菜单项（管理）
- `GET /api/admin/homepage-config` - 获取首页配置
- `PUT /api/admin/homepage-config` - 更新首页配置
- `GET /api/admin/carousel-config` - 获取轮播图配置
- `PUT /api/admin/carousel-config` - 更新轮播图配置
- `POST /api/admin/images/upload` - 上传新图片
- `GET /api/admin/pages/<id>/grid-layout` - 获取网格布局（含合并单元格）
- `POST /api/admin/pages/<id>/grid-layout` - 保存网格布局（含合并单元格）

## 🚀 技术栈

- **后端框架**: Flask 3.0.0
- **数据库**: SQLite (cms.db)
- **前端框架**: Bootstrap 5
- **富文本编辑器**: Quill.js
- **图标**: Font Awesome 6.4.0
- **图片处理**: Pillow 10.0.0
- **国际化**: Flask-Babel
- **拖拽排序**: SortableJS

## 📦 安装

### 前置条件
- Python 3.7+
- pip

### 快速开始

1. **克隆仓库**
```bash
git clone <仓库地址>
cd cms
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **运行应用**
```bash
python app.py
```

4. **访问系统**
- 前台: http://localhost:8080/
- 管理后台: http://localhost:8080/admin/login
- 默认账号: `admin` / `admin`

## 📁 项目结构

```
cms/
├── app.py                      # 主 Flask 应用
├── models.py                   # 数据库模型
├── babel.cfg                   # 翻译配置
├── requirements.txt            # Python 依赖
├── README.md                   # 英文文档
├── README_zh.md               # 中文文档
├── HOMEPAGE_CONTENT_MANAGEMENT.md  # 首页内容管理指南
├── MULTILANG_README.md        # 多语言功能指南
├── GRID_EDITOR_LIBRARY_INTEGRATION.md  # 网格编辑器库集成指南
├── CELL_MERGE_FEATURE.md      # 单元格合并功能指南
├── translations/              # 翻译文件
│   ├── zh_CN/LC_MESSAGES/     # 中文翻译
│   │   ├── messages.po
│   │   └── messages.mo
│   └── en_US/LC_MESSAGES/     # 英文翻译
│       ├── messages.po
│       └── messages.mo
├── static/                    # 静态文件
│   └── uploads/              # 上传文件
│       ├── images/           # 图片文件
│       ├── videos/           # 视频文件
│       └── thumbnails/       # 缩略图
└── templates/                 # Jinja2 模板
    ├── base.html             # 基础模板
    ├── index.html            # 首页
    ├── admin/                # 管理后台模板
    │   ├── base.html
    │   ├── login.html
    │   ├── dashboard.html
    │   ├── articles.html
    │   ├── article_edit.html
    │   ├── videos.html
    │   ├── video_edit.html
    │   ├── images.html
    │   ├── image_upload.html
    │   ├── menu_management.html
    │   ├── links.html
    │   ├── homepage_config.html
    │   ├── homepage_content.html
    │   ├── carousel_management.html
    │   └── dynamic_page_editor.html  # 网格编辑器（含库集成和单元格合并）
    ├── article_detail.html
    ├── video_detail.html
    ├── image_detail.html
    ├── articles_list.html
    ├── videos_list.html
    ├── images_list.html
    ├── dynamic_page.html
    └── grid_page_display.html
```

## 📖 使用指南

### 管理员登录
1. 访问 `/admin/login`
2. 输入用户名: `admin`, 密码: `admin`
3. 点击登录进入管理后台

### 创建文章
1. 登录后，点击侧边栏"文章"
2. 点击"新建文章"
3. 填写标题、内容、分类、标签等
4. 选择发布状态（立即发布或保存为草稿）
5. 点击"保存文章"

### 添加视频
1. 在管理后台，点击"视频"
2. 点击"添加视频"
3. 填写视频信息
4. 输入视频链接（本地路径或外部链接）
5. 保存视频

### 上传图片
1. 在管理后台，点击"图片"
2. 点击"上传图片"
3. 选择图片文件
4. 填写图片信息
5. 上传并保存

### 管理链接
1. 在管理后台，进入"布局管理" > "链接管理"
2. 点击"添加/编辑链接"
3. 填写标题和链接地址
4. 可选添加描述、图标（Font Awesome 类）或分类
5. 设置可见性和状态
6. 拖拽链接进行排序
7. 点击"保存链接"

### 首页内容管理
1. 在管理后台，进入"布局管理" > "首页内容管理"
2. 为每个版块选择内容：
   - **文章版块**: 搜索并选择要显示的文章
   - **视频版块**: 选择要在首页显示的视频
   - **图片版块**: 选择要显示的图片
   - **链接版块**: 选择要展示的链接
3. 使用搜索框过滤内容
4. 点击"+"将内容添加到选择列表
5. 点击"×"从选择列表移除内容
6. 拖拽选择的项目进行排序
7. 点击"保存配置"应用更改

### 轮播图管理
1. 在管理后台，进入"布局管理" > "轮播图管理"
2. 点击"添加轮播图"
3. 从图库选择图片或上传新图片
4. 拖拽排序轮播图片
5. 最多支持5张图片
6. 保存更改

### 动态页面编辑器（网格布局）
1. 在管理后台，进入"动态页面"
2. 点击任意页面的"编辑"或创建新页面
3. 使用网格编辑器构建页面：
   - **添加元素**: 从元素库拖拽元素到网格
   - **库集成**:
     - **图片元素**: 点击"从图库选择"选择现有图片
     - **视频元素**: 点击"从视频库选择"选择现有视频
     - **相册元素**: 点击"选择多张图片"选择多张图片
     - **文本元素**: 点击"引用文章"插入现有文章
   - **单元格合并**:
     - 点击选择单元格（Ctrl/Cmd 多选）
     - 点击"合并单元格"合并所选单元格
     - 点击"取消合并"拆分合并单元格
     - 视觉反馈显示选中的单元格和合并大小
4. 保存页面

### 语言切换
- **前台**: 点击导航栏中的地球图标
- **URL切换**: 访问 `/set_language/en` 或 `/set_language/zh_CN`
- **自动检测**: 系统自动检测浏览器语言偏好

## 🔌 API 示例

### 获取所有文章
```bash
curl http://localhost:8080/api/articles
```

### 获取特定文章
```bash
curl http://localhost:8080/api/articles/my-first-article
```

### 获取所有图片
```bash
curl http://localhost:8080/api/images
```

### 获取所有链接
```bash
curl http://localhost:8080/api/links
```

### 获取首页配置
```bash
curl http://localhost:8080/api/admin/homepage-config
```

### 更新首页配置
```bash
curl -X PUT http://localhost:8080/api/admin/homepage-config \
  -H "Content-Type: application/json" \
  -d '{"config": {...}, "enabled": true}'
```

### 获取网格布局（含合并单元格）
```bash
curl http://localhost:8080/api/admin/pages/1/grid-layout
```

### 保存网格布局（含合并单元格）
```bash
curl -X POST http://localhost:8080/api/admin/pages/1/grid-layout \
  -H "Content-Type: application/json" \
  -d '{"grid": {...}, "mergedCells": {...}}'
```

### 切换到英文（通过URL）
```bash
curl http://localhost:8080/set_language/en
```

## ⚙️ 配置

### 修改管理员密码
编辑 `app.py` 中的登录验证逻辑：
```python
if username == 'admin' and password == 'admin':  # 在此修改密码
    session['admin_logged_in'] = True
```

### 修改数据库
编辑 `models.py`，然后删除 `cms.db` 并重启应用。

### 修改上传文件大小限制
编辑 `app.py`：
```python
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 修改为所需大小
```

### 添加新翻译
1. 标记文本为可翻译：
   - 在模板中: `{% trans %}要翻译的文本{% endtrans %}`
   - 在 Python 中: `gettext("要翻译的文本")`
2. 提取翻译：
   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   ```
3. 更新翻译文件：
   ```bash
   pybabel update -i messages.pot -d translations
   ```
4. 编辑 `.po` 文件添加翻译
5. 编译翻译：
   ```bash
   pybabel compile -d translations
   ```

## 📝 开发说明

### 最近更新
- **网格编辑器库集成**: 在创建页面时直接从现有库选择内容
  - 为图片元素从图库选择图片
  - 为视频元素从视频库选择视频
  - 为相册元素从图库选择多张图片
  - 在文本元素中引用文章
- **单元格合并功能**: 合并和取消合并网格单元格，实现灵活布局
  - 使用 Ctrl/Cmd + 点击多选单元格
  - 将矩形选择合并为更大的单元格
  - 带有选择标识的视觉反馈
  - 合并单元格上的尺寸标识（例如：2x2）
  - 跨保存的持久合并状态
- **首页内容管理**: 选择并排列特定内容在首页显示，支持拖拽排序
- **轮播图管理**: 管理首页横幅图片，支持可排序界面
- **链接管理系统**: 添加、编辑和管理带图标或图片的链接
- **首页链接区域**: 以美观的卡片布局显示链接
- **多语言支持**: 添加中英文切换
- **增强图片管理**: 文章封面图选择器
- **菜单管理**: 支持拖拽排序的分层菜单系统
- **动态页面**: 拖拽式页面编辑器
- **首页配置**: 可自定义首页布局
- **动态语言切换**: 基于会话的语言持久化

### 浏览器缓存说明
- 前台更改可能需要硬刷新（Ctrl+Shift+R）
- 开发期间使用无痕模式避免缓存内容

### 文件组织

**管理后台模板**:
- `homepage_content.html` - 首页内容选择界面
- `carousel_management.html` - 轮播图管理
- `homepage_config.html` - 首页布局配置
- `dynamic_page_editor.html` - 高级网格编辑器（含库集成和单元格合并）

**文档**:
- `HOMEPAGE_CONTENT_MANAGEMENT.md` - 首页内容管理详细指南
- `GRID_EDITOR_LIBRARY_INTEGRATION.md` - 网格编辑器库集成指南
- `CELL_MERGE_FEATURE.md` - 单元格合并功能指南
- `CELL_MERGE_QUICK_GUIDE.md` - 单元格合并快速指南
- `FEATURE_COMPLETION_SUMMARY.md` - 已完成功能摘要

## ⚠️ 重要说明

### 生产部署
1. 修改 `app.py` 中的 `SECRET_KEY`
2. 将 SQLite 替换为 PostgreSQL/MySQL
3. 实现适当的用户认证
4. 添加 CSRF 保护
5. 配置 HTTPS
6. 设置云存储（AWS S3 等）
7. 添加缓存层（Redis/Memcached）
8. 实现速率限制
9. 添加日志和监控

### 文件上传
- 确保 `static/uploads/` 目录有写权限
- 定期清理未使用的文件

### 性能优化
- 使用 CDN 提供图片
- 添加缓存机制
- 使用反向代理（Nginx）
- 启用 gzip 压缩

## 🛣️ 开发路线图

- [ ] 用户认证系统
- [ ] 多用户支持
- [ ] 评论系统
- [ ] SEO 优化
- [ ] 搜索功能
- [ ] 主题系统
- [ ] 插件系统
- [ ] 其他语言（日语、韩语等）
- [ ] RSS 订阅支持
- [ ] 网站地图生成

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目基于 MIT 许可证 - 查看 LICENSE 文件了解详情。

## 👨‍💻 作者

由 taa 使用 Flask 和现代 Web 技术构建。

---

**享受使用 AI-CMS！** 🚀

更多详情，请参阅：
- [`HOMEPAGE_CONTENT_MANAGEMENT.md`](HOMEPAGE_CONTENT_MANAGEMENT.md) - 首页内容管理指南
- [`MULTILANG_README.md`](MULTILANG_README.md) - 多语言功能指南
- [`GRID_EDITOR_LIBRARY_INTEGRATION.md`](GRID_EDITOR_LIBRARY_INTEGRATION.md) - 网格编辑器库集成指南
- [`CELL_MERGE_FEATURE.md`](CELL_MERGE_FEATURE.md) - 单元格合并功能指南
- [`CELL_MERGE_QUICK_GUIDE.md`](CELL_MERGE_QUICK_GUIDE.md) - 单元格合并快速指南
- [`README.md`](README.md) - English Documentation
