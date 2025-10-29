#!/bin/bash

echo "================================"
echo "  推送到GitHub脚本"
echo "================================"
echo ""

# 检查是否在正确的目录
if [ ! -f "app.py" ]; then
    echo "❌ 错误：未找到app.py文件，请确保在CMS项目根目录"
    exit 1
fi

echo "📁 当前目录：$(pwd)"
echo ""

# 检查git是否已初始化
if [ ! -d ".git" ]; then
    echo "🔧 初始化Git仓库..."
    git init
    echo "✅ Git仓库初始化完成"
    echo ""
fi

# 检查远程仓库是否已设置
if ! git remote get-url origin &> /dev/null; then
    echo "⚠️  请输入您的GitHub仓库地址"
    echo "   例如：https://github.com/yourusername/my-cms.git"
    read -p "远程仓库地址: " repo_url
    git remote add origin "$repo_url"
    echo "✅ 远程仓库已添加"
    echo ""
fi

# 添加文件
echo "📦 添加文件到Git..."
git add .
echo "✅ 文件添加完成"
echo ""

# 提交
echo "💾 创建提交..."
read -p "提交信息 (默认: 'Update CMS'): " commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="Update CMS"
fi
git commit -m "$commit_msg"
echo "✅ 提交完成"
echo ""

# 推送到GitHub
echo "🚀 推送到GitHub..."
git branch -M main

# 检查是否使用GitHub CLI
if command -v gh &> /dev/null; then
    gh auth status &> /dev/null
    if [ $? -eq 0 ]; then
        echo "使用GitHub CLI推送..."
        gh repo create --public --push
        return
    fi
fi

# 使用普通git推送
git push -u origin main

echo ""
echo "================================"
echo "✅ 推送完成！"
echo "================================"
echo ""
echo "🌐 查看您的仓库："
git remote get-url origin | sed 's/.git$//'
echo ""
