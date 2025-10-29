#!/bin/bash

echo "检测网络环境..."

# 检查是否能连接GitHub
if curl -s --connect-timeout 5 https://github.com > /dev/null; then
    echo "✅ GitHub连接正常"
else
    echo "❌ 无法连接到GitHub"
    echo ""
    echo "建议解决方案："
    echo "1. 检查网络连接"
    echo "2. 如果在中国，建议配置Git代理："
    echo ""
    echo "设置HTTP代理："
    echo "git config --global http.proxy http://127.0.0.1:7890"
    echo "git config --global https.proxy http://127.0.0.1:7890"
    echo ""
    echo "或者使用GitHub镜像（可能需要）："
    echo "git config --global url \"https://ghproxy.com/https://github.com/\".insteadOf \"https://github.com/\""
    echo ""
fi

echo ""
echo "当前Git配置："
git config --list | grep -E "(remote|user)"
