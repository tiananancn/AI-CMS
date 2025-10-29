#!/usr/bin/env python
"""
创建拖拽式编辑器演示页面
运行此脚本将在数据库中创建一个示例动态页面，包含各种类型的内容块
"""

from app import app, db, DynamicPage, ContentBlock
import json

def create_demo_page():
    """创建演示页面"""
    with app.app_context():
        # 检查是否已存在演示页面
        existing = DynamicPage.query.filter_by(slug='demo-page').first()
        if existing:
            print("演示页面已存在，跳过创建")
            return existing

        # 创建动态页面
        page = DynamicPage(
            title='拖拽式编辑器演示页面',
            slug='demo-page',
            description='这是一个展示拖拽式编辑器功能的演示页面，包含文本、图片、视频、引用等多种内容块。',
            cover_image='',
            status='published'
        )
        db.session.add(page)
        db.session.flush()  # 获取page.id

        # 创建文本块
        text_block1 = ContentBlock(
            page_id=page.id,
            block_type='text',
            sort_order=0
        )
        text_block1.set_content({
            'html': '''
                <h1>欢迎使用拖拽式编辑器</h1>
                <p>这是一个功能强大的所见即所得在线编辑器。您可以通过简单的拖拽操作来创建和编辑页面内容。</p>
                <h2>主要特性</h2>
                <ul>
                    <li>直观的拖拽操作</li>
                    <li>丰富的内容块类型</li>
                    <li>实时预览效果</li>
                    <li>响应式设计</li>
                </ul>
                <p>开始创建您的第一个页面吧！</p>
            '''
        })
        db.session.add(text_block1)

        # 创建图片块
        image_block = ContentBlock(
            page_id=page.id,
            block_type='image',
            sort_order=1
        )
        image_block.set_content({
            'url': '/static/uploads/images/placeholder.jpg',
            'alt': '示例图片'
        })
        db.session.add(image_block)

        # 创建引用块
        quote_block = ContentBlock(
            page_id=page.id,
            block_type='quote',
            sort_order=2
        )
        quote_block.set_content({
            'text': '设计不仅仅关乎外观和感觉。设计关乎它如何运作。',
            'author': '史蒂夫·乔布斯'
        })
        db.session.add(quote_block)

        # 创建分隔线
        divider_block1 = ContentBlock(
            page_id=page.id,
            block_type='divider',
            sort_order=3
        )
        db.session.add(divider_block1)

        # 创建视频块
        video_block = ContentBlock(
            page_id=page.id,
            block_type='video',
            sort_order=4
        )
        video_block.set_content({
            'url': '/static/uploads/videos/demo.mp4'
        })
        db.session.add(video_block)

        # 创建另一个文本块
        text_block2 = ContentBlock(
            page_id=page.id,
            block_type='text',
            sort_order=5
        )
        text_block2.set_content({
            'html': '''
                <h2>如何开始</h2>
                <ol>
                    <li><strong>登录管理后台</strong> - 使用 admin/admin 登录</li>
                    <li><strong>创建新页面</strong> - 点击"新建页面"按钮</li>
                    <li><strong>进入编辑器</strong> - 点击"拖拽编辑"按钮</li>
                    <li><strong>添加内容块</strong> - 使用工具栏按钮添加不同类型的内容</li>
                    <li><strong>拖拽排序</strong> - 拖拽调整内容块的顺序</li>
                    <li><strong>编辑内容</strong> - 点击编辑按钮修改内容</li>
                    <li><strong>保存发布</strong> - 预览满意后发布页面</li>
                </ol>
                <blockquote>
                    <p>提示：所有更改都会自动保存，您可以随时预览效果。</p>
                </blockquote>
            '''
        })
        db.session.add(text_block2)

        # 创建文章引用块
        article_block = ContentBlock(
            page_id=page.id,
            block_type='article',
            sort_order=6
        )
        article_block.set_content({
            'articleId': 1
        })
        db.session.add(article_block)

        # 创建分隔线
        divider_block2 = ContentBlock(
            page_id=page.id,
            block_type='divider',
            sort_order=7
        )
        db.session.add(divider_block2)

        # 创建最后一个文本块
        text_block3 = ContentBlock(
            page_id=page.id,
            block_type='text',
            sort_order=8
        )
        text_block3.set_content({
            'html': '''
                <h2>联系信息</h2>
                <p>如有任何问题或建议，欢迎联系我们：</p>
                <p>📧 Email: admin@example.com</p>
                <p>📱 电话: 123-456-7890</p>
                <p>🌐 网站: <a href="https://example.com">www.example.com</a></p>
            '''
        })
        db.session.add(text_block3)

        db.session.commit()
        print(f"✅ 演示页面创建成功！")
        print(f"   页面ID: {page.id}")
        print(f"   页面标题: {page.title}")
        print(f"   页面别名: {page.slug}")
        print(f"   前台访问地址: http://localhost:8080/page/{page.slug}")
        print(f"   管理后台地址: http://localhost:8080/admin/dynamic_pages")

        return page

if __name__ == '__main__':
    create_demo_page()
