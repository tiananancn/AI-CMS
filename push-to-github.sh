#!/bin/bash

# GitHub推送脚本
# 配置SSH密钥后运行此脚本即可一键推送

echo "=================================="
echo "  GitHub 推送脚本"
echo "=================================="
echo ""

# 测试SSH连接
echo "🔍 测试SSH连接到GitHub..."
ssh -T git@github.com 2>&1

# 检查返回码
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ SSH连接成功！"
    echo "🚀 正在推送代码到GitHub..."
    echo ""

    # 推送代码
    git push origin main

    if [ $? -eq 0 ]; then
        echo ""
        echo "🎉 推送成功！"
        echo "=================================="
    else
        echo ""
        echo "❌ 推送失败，请检查错误信息"
        exit 1
    fi
else
    echo ""
    echo "❌ SSH连接失败！"
    echo ""
    echo "请确认："
    echo "1. 已在GitHub添加SSH密钥: https://github.com/settings/keys"
    echo "2. 使用正确的GitHub账户登录"
    echo "3. 等待几分钟让密钥生效"
    echo ""
    echo "SSH密钥信息："
    ssh-keygen -l -f ~/.ssh/id_ed25519
    exit 1
fi
