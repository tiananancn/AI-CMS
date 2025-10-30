# AI-CMS 智能内容管理系统 🎯

[![English](https://img.shields.io/badge/Language-English-blue.svg)](README.md)
[![中文](https://img.shields.io/badge/语言-中文-red.svg)](README_zh.md)
[![Python](https://img.shields.io/badge/Python-3.7+-green.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个基于Flask开发的轻量级且功能强大的内容管理系统（CMS），支持文章、视频和图片管理，具有美观的后台管理界面和灵活的前台展示功能。

## ✨ 功能特性

### 🎨 前台功能
- **首页展示**：展示最新的文章、视频和图片
- **文章系统**：
  - 文章列表页（支持分页和分类筛选）
  - 文章详情页（支持富文本内容）
  - 文章分类和标签系统
  - 封面图片支持
- **视频系统**：
  - 视频列表页（支持分页和分类筛选）
  - 视频详情页（支持本地视频和外部链接）
  - 视频分类和标签系统
- **图片系统**：
  - 图片网格展示
  - 图片详情页
  - 图片下载功能
  - 图片模态框预览

### 🛠️ 后台管理
- **仪表盘**：显示系统统计数据
- **文章管理**：
  - 创建、编辑、删除文章
  - 支持富文本编辑器（Quill）
  - 文章状态管理（发布/草稿）
  - 分类和标签管理
  - 封面图片选择器
- **视频管理**：
  - 添加、编辑、删除视频
  - 支持本地视频文件和外部链接（YouTube、Bilibili等）
  - 视频状态管理
  - 分类和标签管理
- **图片管理**：
  - 图片上传功能
  - 图片预览
  - 图片信息展示
  - 分类和标签管理
- **菜单管理**：支持拖拽排序的动态导航菜单
- **首页配置**：可定制的首页布局
- **动态页面**：拖拽式页面编辑器

### 🌍 多语言支持
- **内置语言切换**：在中英文之间自由切换
- **自动检测**：自动检测浏览器语言偏好
- **会话持久化**：保存用户语言选择
- **翻译管理**：基于Flask-Babel的翻译系统

### 📊 RESTful API
系统提供完整的RESTful API接口：
- `GET /api/articles` - 获取所有文章
- `GET /api/articles/<slug>` - 获取特定文章
- `GET /api/videos` - 获取所有视频
- `GET /api/videos/<slug>` - 获取特定视频
- `GET /api/images` - 获取所有图片
- `GET /api/images/<slug>` - 获取特定图片
- `GET /api/menu-items` - 获取菜单项
- `GET /api/admin/menu-items` - 获取所有菜单项（管理后台）

## 🚀 技术栈

- **后端框架**：Flask 3.0.0
- **数据库**：SQLite (CMS.db)
- **前端框架**：Bootstrap 5
- **富文本编辑器**：Quill.js
- **图标**：Font Awesome 6.4.0
- **图像处理**：Pillow
- **国际化**：Flask-Babel

## 📦 安装说明

### 环境要求
- Python 3.7+
- pip

### 快速开始

1. **克隆项目**
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
- 前台首页：http://localhost:8080
- 后台管理：http://localhost:8080/admin/login
- 默认管理员账号：`admin` / `admin`

## 📁 项目结构

```
cms/
├── app.py                      # Flask主应用
├── models.py                   # 数据库模型
├── babel.cfg                   # 翻译配置文件
├── requirements.txt            # Python依赖
├── README.md                   # 英文文档
├── README_zh.md               # 中文文档
├── MULTILANG_README.md        # 多语言功能指南
├── translations/              # 翻译文件目录
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
└── templates/                 # Jinja2模板
    ├── base.html             # 基础模板
    ├── index.html            # 首页
    ├── admin/                # 后台模板
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
    │   ├── homepage_config.html
    │   ├── dynamic_pages.html
    │   └── dynamic_page_edit.html
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
2. 输入用户名：`admin`，密码：`admin`
3. 点击登录进入管理后台

### 创建文章
1. 登录后台后，点击侧边栏「文章」
2. 点击「新建文章」
3. 填写标题、内容、分类、标签等信息
4. 选择发布状态（立即发布/保存为草稿）
5. 点击「保存文章」

### 添加视频
1. 在后台点击「视频」
2. 点击「添加视频」
3. 填写视频信息
4. 输入视频URL（支持本地路径或外部链接）
5. 保存视频

### 上传图片
1. 在后台点击「图片」
2. 点击「上传图片」
3. 选择图片文件
4. 填写图片信息
5. 上传并保存

### 语言切换
- **前端切换**：点击导航栏的地球图标
- **URL切换**：访问 `/set_language/en` 或 `/set_language/zh_CN`
- **自动检测**：系统会自动检测浏览器语言偏好

## 🔌 API使用示例

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

### 切换到英文（通过URL）
```bash
curl http://localhost:8080/set_language/en
```

## ⚙️ 自定义配置

### 修改管理员密码
编辑 `app.py` 文件中的登录验证逻辑：
```python
if username == 'admin' and password == 'admin':  # 修改这里的密码
    session['admin_logged_in'] = True
```

### 修改数据库
编辑 `models.py` 文件，然后删除 `cms.db` 文件重新运行应用。

### 修改上传文件大小限制
编辑 `app.py` 文件：
```python
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 修改为你需要的大小
```

### 添加新翻译
1. 标记需要翻译的文本：
   - 模板中：`{% trans %}要翻译的文本{% endtrans %}`
   - Python中：`gettext("要翻译的文本")`
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
- **多语言支持**：添加中英文切换功能
- **增强图片管理**：文章封面图片选择器
- **动态页面编辑器**：拖拽式页面构建器
- **菜单管理**：支持拖拽排序的层级菜单系统
- **首页配置**：可定制的首页布局

### 浏览器缓存注意事项
- 前端修改可能需要强制刷新（Ctrl+Shift+R）
- 开发时建议使用无痕模式避免缓存

## ⚠️ 注意事项

### 生产环境部署
1. 修改 `app.py` 中的 `SECRET_KEY`
2. 将SQLite替换为PostgreSQL/MySQL
3. 实现更安全的用户认证系统
4. 添加CSRF保护
5. 配置HTTPS
6. 设置云存储（如AWS S3）
7. 添加缓存层（Redis/Memcached）
8. 实现速率限制
9. 添加日志和监控

### 文件上传
- 确保 `static/uploads` 目录有写权限
- 定期清理未使用的文件

### 性能优化
- 图片可使用CDN加速
- 添加缓存机制
- 使用反向代理（如Nginx）
- 启用gzip压缩

## 🛣️ 开发计划

- [ ] 用户认证系统
- [ ] 多用户支持
- [ ] 评论系统
- [ ] SEO优化
- [ ] 搜索功能
- [ ] 主题系统
- [ ] 插件系统
- [ ] 更多语言（日语、韩语等）
- [ ] RSS订阅支持
- [ ] 站点地图生成

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

本项目使用MIT许可证 - 查看LICENSE文件了解详情。

## 👨‍💻 作者

使用Flask和现代Web技术精心打造。

---

**享受使用AI-CMS！** 🚀

更多详细信息请查看：
- [`MULTILANG_README.md`](MULTILANG_README.md) - 多语言功能指南
- [`README.md`](README.md) - English Documentation
