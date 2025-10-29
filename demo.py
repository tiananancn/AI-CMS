#!/usr/bin/env python3
"""
CMS系统演示脚本
展示如何使用API添加和获取内容
"""

import requests
import json

BASE_URL = "http://localhost:8080"

def demo_api():
    """演示API使用"""
    print("\n" + "="*50)
    print("CMS API 演示")
    print("="*50)

    # 1. 获取所有文章
    print("\n1. 获取所有文章:")
    response = requests.get(f"{BASE_URL}/api/articles")
    articles = response.json()
    print(f"   共找到 {len(articles)} 篇文章")
    if articles:
        print(f"   最新文章: {articles[0].get('title', 'N/A')}")

    # 2. 获取所有视频
    print("\n2. 获取所有视频:")
    response = requests.get(f"{BASE_URL}/api/videos")
    videos = response.json()
    print(f"   共找到 {len(videos)} 个视频")
    if videos:
        print(f"   最新视频: {videos[0].get('title', 'N/A')}")

    # 3. 获取所有图片
    print("\n3. 获取所有图片:")
    response = requests.get(f"{BASE_URL}/api/images")
    images = response.json()
    print(f"   共找到 {len(images)} 张图片")
    if images:
        print(f"   最新图片: {images[0].get('title', 'N/A')}")

    print("\n" + "="*50)
    print("演示完成!")
    print("="*50 + "\n")

def demo_frontend():
    """演示前端功能"""
    print("\n" + "="*50)
    print("前端页面演示")
    print("="*50)
    print(f"\n前台首页: {BASE_URL}")
    print(f"后台登录: {BASE_URL}/admin/login")
    print(f"文章列表: {BASE_URL}/articles")
    print(f"视频列表: {BASE_URL}/videos")
    print(f"图片列表: {BASE_URL}/images")
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    try:
        # 检查服务是否运行
        response = requests.get(BASE_URL, timeout=2)
        if response.status_code == 200:
            print("\n✓ CMS系统正在运行\n")
            demo_api()
            demo_frontend()
        else:
            print("✗ CMS系统未正常运行")
    except requests.exceptions.RequestException:
        print("✗ 无法连接到CMS系统，请先启动应用:")
        print(f"  python3 {__file__.replace('demo.py', 'app.py')}")
