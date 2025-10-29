#!/bin/bash

echo "================================"
echo "   我的CMS系统启动脚本"
echo "================================"
echo ""

# 检查Python版本
echo "检查Python版本..."
python3 --version

# 检查依赖
echo ""
echo "检查依赖包..."
if ! pip3 list | grep -q "Flask"; then
    echo "正在安装依赖包..."
    pip3 install -r requirements.txt
else
    echo "依赖包已安装"
fi

echo ""
echo "启动CMS系统..."
echo "前台地址: http://localhost:8080"
echo "后台地址: http://localhost:8080/admin/login"
echo "默认账号: admin / admin"
echo ""
echo "按 Ctrl+C 停止服务器"
echo "================================"
echo ""

python3 app.py
