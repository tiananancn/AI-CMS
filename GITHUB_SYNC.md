# 🚀 GitHub 同步指南

本指南将帮助您将CMS项目推送到GitHub。

## 方法一：使用自动推送脚本（推荐）

### 1. 运行脚本
```bash
./push_to_github.sh
```

### 2. 按照提示操作
- 输入GitHub仓库地址（如：https://github.com/username/my-cms.git）
- 输入提交信息（可选）
- 脚本会自动完成所有操作

---

## 方法二：手动推送

### 第一步：在GitHub创建仓库

1. 访问 [GitHub](https://github.com) 并登录
2. 点击右上角 **"+"** → **"New repository"**
3. 填写仓库信息：
   - **Repository name**: `my-cms` 或其他名称
   - **Description**: `A Beautiful Content Management System`
   - 选择 **Public** 或 **Private**
   - **不要**勾选 "Add a README file"
   - 点击 **"Create repository"**

### 第二步：本地Git操作

```bash
# 进入项目目录
cd /Users/taataa/Documents/taa/private/python/cms

# 1. 初始化Git（如果还没初始化）
git init

# 2. 添加.gitignore文件（已创建）
# 确保.gitignore在项目根目录

# 3. 添加所有文件
git add .

# 4. 创建提交
git commit -m "Initial commit: Complete CMS system

✨ Features:
- Beautiful admin dashboard with Bootstrap 5
- Article management with Quill.js rich text editor
- Video management (local & external URLs)
- Image upload system with preview
- RESTful API endpoints
- Responsive frontend design
- Category & tag system
- Pagination support

🛠️ Tech Stack:
- Backend: Flask + SQLAlchemy
- Database: SQLite
- Frontend: Bootstrap 5 + Font Awesome
- Editor: Quill.js
- File Upload: Werkzeug"

# 5. 添加GitHub远程仓库
# 替换为您的实际仓库地址
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 6. 推送到GitHub
git branch -M main
git push -u origin main
```

---

## 🔑 认证方式

### 方式1：Personal Access Token（推荐）

1. **创建Token**：
   - GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - 点击 "Generate new token"
   - 勾选 `repo` 权限
   - 复制生成的token

2. **推送时认证**：
   - 用户名：您的GitHub用户名
   - 密码：粘贴您的Personal Access Token（不是GitHub密码）

### 方式2：GitHub CLI

```bash
# 安装GitHub CLI (如果还没安装)
# macOS: brew install gh

# 登录
gh auth login

# 推送
git push -u origin main
```

### 方式3：SSH（高级用户）

```bash
# 生成SSH密钥
ssh-keygen -t ed25519 -C "your_email@example.com"

# 添加SSH密钥到GitHub
# Settings → SSH and GPG keys → New SSH key

# 使用SSH地址推送
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

---

## 📁 .gitignore 说明

项目已包含 `.gitignore` 文件，会自动忽略：
- Python编译文件 (`__pycache__/`)
- 虚拟环境目录 (`venv/`, `env/`)
- 数据库文件 (`*.db`, `*.sqlite3`)
- 上传的文件 (`static/uploads/*`)
- IDE配置文件 (`.vscode/`, `.idea/`)
- 系统文件 (`.DS_Store`)

---

## 🔄 后续更新

推送成功后，以后更新代码只需：

```bash
# 添加修改
git add .

# 提交
git commit -m "Describe your changes"

# 推送到GitHub
git push
```

---

## 🌐 查看仓库

推送成功后，在浏览器中访问：
```
https://github.com/YOUR_USERNAME/YOUR_REPO_NAME
```

---

## 🎉 完成！

您的CMS项目现在已经在GitHub上了！

**接下来可以做的：**
- [ ] 添加项目描述和截图到GitHub仓库
- [ ] 启用GitHub Pages部署静态版本
- [ ] 创建Release版本
- [ ] 添加Contributing指南
- [ ] 添加License文件

---

## ❓ 常见问题

**Q: 推送时提示认证失败？**
A: 使用Personal Access Token代替密码登录

**Q: 想要私有仓库？**
A: 在GitHub创建仓库时选择"Private"

**Q: 如何撤销最后一次提交？**
A: `git reset --soft HEAD~1` (保留修改) 或 `git reset --hard HEAD~1` (丢弃修改)

**Q: 如何更新远程仓库地址？**
A: `git remote set-url origin NEW_URL`

---

## 📚 更多资源

- [GitHub官方文档](https://docs.github.com)
- [Git常用命令](https://git-scm.com/docs)
- [GitHub CLI文档](https://cli.github.com/manual)
