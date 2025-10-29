# 我的CMS系统

一个基于Flask开发的轻量级内容管理系统（CMS），支持文章、视频和图片管理，具有美观的后台管理界面和灵活的前台展示功能。

## 功能特性

### 🎨 前台功能
- **首页展示**：展示最新的文章、视频和图片
- **文章系统**：
  - 文章列表页（支持分页和分类筛选）
  - 文章详情页（支持富文本内容）
  - 文章分类和标签系统
- **视频系统**：
  - 视频列表页（支持分页和分类筛选）
  - 视频详情页（支持本地视频和外部链接）
  - 视频分类和标签系统
- **图片系统**：
  - 图片网格展示
  - 图片详情页
  - 图片下载功能
  - 图片模态框预览

### 🔧 后台管理
- **仪表盘**：显示系统统计数据
- **文章管理**：
  - 创建、编辑、删除文章
  - 支持富文本编辑器（Quill）
  - 文章状态管理（发布/草稿）
  - 分类和标签管理
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

### 📊 API接口
系统提供完整的RESTful API接口：
- `GET /api/articles` - 获取所有文章
- `GET /api/articles/<slug>` - 获取特定文章
- `GET /api/videos` - 获取所有视频
- `GET /api/videos/<slug>` - 获取特定视频
- `GET /api/images` - 获取所有图片
- `GET /api/images/<slug>` - 获取特定图片

## 技术栈

- **后端框架**：Flask
- **数据库**：SQLite
- **前端框架**：Bootstrap 5
- **富文本编辑器**：Quill.js
- **图标**：Font Awesome

## 安装说明

### 环境要求
- Python 3.7+
- pip

### 安装步骤

1. **克隆项目**
```bash
cd /Users/taataa/Documents/taa/private/python/cms
```

2. **安装依赖**
```bash
pip install flask flask-sqlalchemy werkzeug
```

3. **运行应用**
```bash
python app.py
```

4. **访问系统**
- 前台首页：http://localhost:5000
- 后台管理：http://localhost:5000/admin/login
- 默认管理员账号：admin / admin

## 项目结构

```
cms/
├── app.py                 # Flask主应用
├── models.py              # 数据库模型
├── README.md              # 说明文档
├── static/                # 静态文件
│   ├── css/               # 样式文件
│   ├── js/                # JavaScript文件
│   └── uploads/           # 上传文件
│       ├── images/        # 图片文件
│       ├── videos/        # 视频文件
│       └── thumbnails/    # 缩略图
└── templates/             # 模板文件
    ├── admin/             # 后台模板
    │   ├── base.html
    │   ├── login.html
    │   ├── dashboard.html
    │   ├── articles.html
    │   ├── article_edit.html
    │   ├── videos.html
    │   ├── video_edit.html
    │   ├── images.html
    │   └── image_upload.html
    ├── base.html          # 基础模板
    ├── index.html         # 首页
    ├── article_detail.html
    ├── video_detail.html
    ├── image_detail.html
    ├── articles_list.html
    ├── videos_list.html
    └── images_list.html
```

## 使用指南

### 管理员登录
1. 访问 `/admin/login`
2. 输入用户名：`admin`，密码：`admin`
3. 点击登录进入管理后台

### 创建文章
1. 登录后台后，点击「文章管理」
2. 点击「新建文章」
3. 填写标题、内容、分类、标签等信息
4. 选择发布状态（立即发布/保存为草稿）
5. 点击「保存文章」

### 添加视频
1. 在后台点击「视频管理」
2. 点击「添加视频」
3. 填写视频信息
4. 输入视频URL（支持本地路径或外部链接）
5. 保存视频

### 上传图片
1. 在后台点击「图片管理」
2. 点击「上传图片」
3. 选择图片文件
4. 填写图片信息
5. 上传并保存

## API使用示例

### 获取所有文章
```bash
curl http://localhost:5000/api/articles
```

### 获取特定文章
```bash
curl http://localhost:5000/api/articles/my-first-article
```

### 获取所有图片
```bash
curl http://localhost:5000/api/images
```

## 自定义配置

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

## 注意事项

1. **生产环境部署**：
   - 修改 `SECRET_KEY`
   - 使用更强的密码
   - 使用更安全的数据库（如PostgreSQL）
   - 配置HTTPS

2. **文件上传**：
   - 确保 `static/uploads` 目录有写权限
   - 定期清理未使用的文件

3. **性能优化**：
   - 图片可以使用CDN加速
   - 添加缓存机制
   - 使用反向代理（如Nginx）

## 开发计划

- [ ] 用户认证系统
- [ ] 多用户支持
- [ ] 评论系统
- [ ] SEO优化
- [ ] 搜索功能
- [ ] 主题系统
- [ ] 插件系统

## 许可证

MIT License

## 联系作者
taa
