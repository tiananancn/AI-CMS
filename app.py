from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, gettext, ngettext
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Article, Video, Image, DynamicPage, ContentBlock, HomepageConfig, MenuItem
from datetime import datetime
import os
import uuid
import imghdr
import re
from functools import wraps

# 检查Base64图片大小
def check_base64_images(content):
    """检查HTML内容中的Base64图片大小"""
    if not content:
        return True, None

    # 查找所有Base64图片
    base64_pattern = r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+'
    matches = re.findall(base64_pattern, content)

    max_single_size = 500 * 1024  # 500KB per image
    total_size = 0

    for match in matches:
        # 计算Base64解码后的大小
        base64_data = match.split(',')[1]
        decoded_size = len(base64_data) * 3 / 4  # Base64解码后的近似大小

        if decoded_size > max_single_size:
            return False, f"单个图片过大 ({decoded_size / 1024:.1f}KB)，建议小于 {max_single_size / 1024}KB"

        total_size += decoded_size

    # 限制总大小
    if total_size > 2 * 1024 * 1024:  # 2MB total
        return False, f"文章中图片总大小过大 ({total_size / 1024 / 1024:.1f}MB)，建议小于 2MB"

    return True, None

# 创建上传目录
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(f'{UPLOAD_FOLDER}/images', exist_ok=True)
os.makedirs(f'{UPLOAD_FOLDER}/videos', exist_ok=True)
os.makedirs(f'{UPLOAD_FOLDER}/thumbnails', exist_ok=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 增加上传文件大小限制到1GB
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024  # 1GB max file size
# 添加请求大小限制配置
app.config['MAX_REQUEST_LENGTH'] = 1024 * 1024 * 1024  # 1GB

# 允许的文件扩展名
app.config['ALLOWED_EXTENSIONS'] = {
    'images': {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp', 'svg'},
    'videos': {'mp4', 'avi', 'mov', 'wmv', 'flv', 'webm', 'mkv'},
}

# 初始化数据库
db.init_app(app)

# ==================== 多语言支持配置 ====================

# 支持的语言
LANGUAGES = {
    'zh_CN': '中文',
    'en': 'English'
}

# 菜单翻译映射
MENU_TRANSLATIONS = {
    'zh_CN': {'首页': '首页', '文章': '文章', '视频': '视频', '图片': '图片', '其它': '其它'},
    'en': {'首页': 'Home', '文章': 'Articles', '视频': 'Videos', '图片': 'Images', '其它': 'Others'}
}

# 首页配置翻译映射
HOMEPAGE_CONFIG_TRANSLATIONS = {
    'zh_CN': {
        '欢迎来到AI-CMS': '欢迎来到AI-CMS',
        '智能内容管理系统，让创作更简单': '智能内容管理系统，让创作更简单',
        '阅读文章': '阅读文章',
        '观看视频': '观看视频',
        '最新文章': '最新文章',
        '最新视频': '最新视频',
        '最新图片': '最新图片',
    },
    'en': {
        '欢迎来到AI-CMS': 'Welcome to AI-CMS',
        '智能内容管理系统，让创作更简单': 'Intelligent Content Management System that makes creation easier',
        '阅读文章': 'Read Articles',
        '观看视频': 'Watch Videos',
        '最新文章': 'Latest Articles',
        '最新视频': 'Latest Videos',
        '最新图片': 'Latest Images',
    }
}

# 语言检测函数
def get_locale():
    """检测当前语言优先级：URL参数 > Session > 浏览器Accept-Language > 默认中文"""
    # 优先级1: URL参数 (通过/set_language/<lang>设置)
    if 'lang' in session:
        return session['lang']

    # 优先级2: 浏览器Accept-Language头
    accept_language = request.headers.get('Accept-Language', '')
    if accept_language:
        # 简单检查是否包含英文
        if accept_language.lower().startswith('en'):
            return 'en'

    # 优先级3: 默认中文
    return 'zh_CN'

# 初始化Babel
babel = Babel(app, locale_selector=get_locale)

# 初始化首页配置（如果不存在）
def init_homepage_config():
    """初始化默认首页配置"""
    config = HomepageConfig.query.filter_by(name='default').first()
    if not config:
        config = HomepageConfig(
            name='default',
            enabled=True
        )
        # 设置默认布局：hero -> articles -> videos -> images
        default_config = {
            'sections': [
                {'type': 'hero', 'visible': True, 'order': 0},
                {'type': 'articles', 'visible': True, 'order': 1, 'title': '最新文章', 'limit': 6},
                {'type': 'videos', 'visible': True, 'order': 2, 'title': '最新视频', 'limit': 6},
                {'type': 'images', 'visible': True, 'order': 3, 'title': '最新图片', 'limit': 8}
            ],
            'hero': {
                'title': '欢迎来到AI-CMS',
                'subtitle': '智能内容管理系统，让创作更简单',
                'show_buttons': True,
                'button1_text': '阅读文章',
                'button1_link': '/articles',
                'button2_text': '观看视频',
                'button2_link': '/videos'
            }
        }
        config.set_config(default_config)
        db.session.add(config)
        db.session.commit()

# 初始化菜单项（如果不存在）
def init_menu_items():
    """初始化默认菜单项"""
    # 检查是否已存在菜单项
    if MenuItem.query.count() > 0:
        return

    # 创建默认菜单项
    default_menus = [
        {'label': '首页', 'url': '/', 'icon': 'fas fa-home', 'order': 0},
        {'label': '文章', 'url': '/articles', 'icon': 'fas fa-newspaper', 'order': 1},
        {'label': '视频', 'url': '/videos', 'icon': 'fas fa-video', 'order': 2},
        {'label': '图片', 'url': '/images', 'icon': 'fas fa-images', 'order': 3},
    ]

    for menu_data in default_menus:
        menu_item = MenuItem(
            label=menu_data['label'],
            url=menu_data['url'],
            icon=menu_data['icon'],
            order=menu_data['order'],
            visible=True
        )
        db.session.add(menu_item)

    db.session.commit()

# 应用启动时初始化配置
with app.app_context():
    db.create_all()
    init_homepage_config()
    init_menu_items()

# 预处理请求
@app.before_request
def before_request():
    """在请求前检查大小"""
    if request.method == 'POST':
        # 检查Content-Length
        content_length = request.headers.get('Content-Length')
        if content_length:
            try:
                length = int(content_length)
                max_length = 50 * 1024 * 1024  # 50MB
                if length > max_length:
                    abort(413)  # Payload Too Large
            except (ValueError, TypeError):
                pass

        # 检查表单数据中的大图片
        if 'content' in request.form:
            content = request.form['content']
            is_valid, error_msg = check_base64_images(content)
            if not is_valid:
                flash(f'文章内容错误: {error_msg}', 'error')
                return redirect(request.referrer or url_for('admin_articles'))

# 文件扩展名检查
def allowed_file(filename, file_type='images'):
    """检查文件扩展名是否允许"""
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in app.config['ALLOWED_EXTENSIONS'][file_type]

# 文件类型验证
def validate_file_type(file_path, expected_type=None):
    """验证文件实际类型"""
    if not os.path.exists(file_path):
        return False

    if expected_type == 'image':
        return imghdr.what(file_path) is not None
    elif expected_type == 'video':
        # 简单的视频文件检查
        video_extensions = {'.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv'}
        _, ext = os.path.splitext(file_path)
        return ext.lower() in video_extensions
    return True

# 登录装饰器
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# ==================== 语言切换路由 ====================

@app.route('/set_language/<lang>')
def set_language(lang):
    """设置语言并重定向到上一页"""
    if lang in LANGUAGES:
        session['lang'] = lang
        referrer = request.referrer or url_for('index')
        return redirect(referrer)
    else:
        flash('不支持的语言', 'error')
        return redirect(url_for('index'))

# 全局模板上下文 - 添加菜单数据和语言选项
@app.context_processor
def inject_menu_items():
    """为所有模板注入菜单数据和语言选项"""
    try:
        current_language = get_locale()
        menu_items = MenuItem.query.filter_by(parent_id=None, visible=True).order_by(MenuItem.order).all()

        # 翻译菜单项
        translated_menu = []
        for item in menu_items:
            translated_label = MENU_TRANSLATIONS.get(current_language, {}).get(item.label, item.label)

            # 获取子菜单
            children = MenuItem.query.filter_by(parent_id=item.id, visible=True).order_by(MenuItem.order).all()
            translated_children = []
            for child in children:
                child_translated_label = MENU_TRANSLATIONS.get(current_language, {}).get(child.label, child.label)
                child_dict = child.to_dict() if hasattr(child, 'to_dict') else {
                    'id': child.id,
                    'label': child_translated_label,
                    'url': child.url,
                    'icon': child.icon,
                    'order': child.order,
                    'visible': child.visible,
                    'parent_id': child.parent_id
                }
                translated_children.append(child_dict)

            # 主菜单项
            item_dict = item.to_dict() if hasattr(item, 'to_dict') else {
                'id': item.id,
                'label': translated_label,
                'url': item.url,
                'icon': item.icon,
                'order': item.order,
                'visible': item.visible,
                'parent_id': item.parent_id
            }
            item_dict['label'] = translated_label
            item_dict['children'] = translated_children
            translated_menu.append(item_dict)

        return {
            'menu_items': translated_menu,
            'LANGUAGES': LANGUAGES,
            'current_lang': current_language
        }
    except:
        # 如果数据库表还不存在，返回空列表，但必须包含LANGUAGES
        return {
            'menu_items': [],
            'LANGUAGES': LANGUAGES,
            'current_lang': get_locale()
        }

# 生成唯一slug
def generate_slug(title, model):
    base_slug = ''.join(c for c in title.lower() if c.isalnum() or c == '-').strip('-')
    slug = base_slug
    counter = 1
    while model.query.filter_by(slug=slug).first():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug

# 首页 - 支持可定制布局
@app.route('/')
def index():
    # 获取首页配置
    config = HomepageConfig.query.filter_by(name='default', enabled=True).first()
    if not config:
        # 如果没有配置，使用默认布局
        latest_articles = Article.query.filter_by(status='published').order_by(Article.created_at.desc()).limit(6).all()
        latest_videos = Video.query.filter_by(status='published').order_by(Video.created_at.desc()).limit(6).all()
        latest_images = Image.query.filter_by(status='published').order_by(Image.created_at.desc()).limit(6).all()
        return render_template('index.html',
                             articles=latest_articles,
                             videos=latest_videos,
                             images=latest_images,
                             hero_config=None,
                             sections=None)

    config_data = config.get_config()
    sections = config_data.get('sections', [])
    hero_config = config_data.get('hero', None)

    # 应用翻译到sections
    current_language = get_locale()
    for section in sections:
        if 'title' in section:
            section['title'] = HOMEPAGE_CONFIG_TRANSLATIONS.get(current_language, {}).get(
                section['title'], section['title']
            )

    # 应用翻译到hero_config
    if hero_config:
        translated_hero = {}
        for key, value in hero_config.items():
            if key in ['title', 'subtitle', 'button1_text', 'button2_text']:
                translated_hero[key] = HOMEPAGE_CONFIG_TRANSLATIONS.get(current_language, {}).get(value, value)
            else:
                translated_hero[key] = value
        hero_config = translated_hero

    # 根据配置获取数据
    data = {}
    for section in sections:
        if not section.get('visible', True):
            continue

        section_type = section.get('type')
        limit = section.get('limit', 6)

        if section_type == 'articles':
            data['articles'] = Article.query.filter_by(status='published').order_by(Article.created_at.desc()).limit(limit).all()
        elif section_type == 'videos':
            data['videos'] = Video.query.filter_by(status='published').order_by(Video.created_at.desc()).limit(limit).all()
        elif section_type == 'images':
            data['images'] = Image.query.filter_by(status='published').order_by(Image.created_at.desc()).limit(limit).all()

    # 按order排序sections
    sorted_sections = sorted(sections, key=lambda x: x.get('order', 0))

    return render_template('index.html',
                         hero_config=hero_config,
                         sections=sorted_sections,
                         **data)

# 文章详情页
@app.route('/article/<slug>')
def article_detail(slug):
    article = Article.query.filter_by(slug=slug, status='published').first_or_404()
    article.views += 1
    db.session.commit()
    return render_template('article_detail.html', article=article)

# 视频详情页
@app.route('/video/<slug>')
def video_detail(slug):
    video = Video.query.filter_by(slug=slug, status='published').first_or_404()
    video.views += 1
    db.session.commit()
    return render_template('video_detail.html', video=video)

# 图片详情页
@app.route('/image/<slug>')
def image_detail(slug):
    image = Image.query.filter_by(slug=slug, status='published').first_or_404()
    image.views += 1
    db.session.commit()
    return render_template('image_detail.html', image=image)

# 博客列表页
@app.route('/articles')
def articles_list():
    category = request.args.get('category', '')
    page = request.args.get('page', 1, type=int)
    query = Article.query.filter_by(status='published')
    if category:
        query = query.filter_by(category=category)
    articles = query.order_by(Article.created_at.desc()).paginate(
        per_page=10, error_out=False
    )
    return render_template('articles_list.html', articles=articles, category=category)

# 视频列表页
@app.route('/videos')
def videos_list():
    category = request.args.get('category', '')
    page = request.args.get('page', 1, type=int)
    query = Video.query.filter_by(status='published')
    if category:
        query = query.filter_by(category=category)
    videos = query.order_by(Video.created_at.desc()).paginate(
        per_page=10, error_out=False
    )
    return render_template('videos_list.html', videos=videos, category=category)

# 图片列表页
@app.route('/images')
def images_list():
    category = request.args.get('category', '')
    page = request.args.get('page', 1, type=int)
    query = Image.query.filter_by(status='published')
    if category:
        query = query.filter_by(category=category)
    images = query.order_by(Image.created_at.desc()).paginate(
        per_page=12, error_out=False
    )
    return render_template('images_list.html', images=images, category=category)

# ==================== 后台管理路由 ====================

# 管理员登录
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 简单的管理员验证（生产环境中应使用更安全的方式）
        if username == 'admin' and password == 'admin':
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('用户名或密码错误', 'error')
    return render_template('admin/login.html')

# 管理员退出
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

# 管理员首页
@app.route('/admin')
@login_required
def admin_dashboard():
    stats = {
        'articles': Article.query.count(),
        'videos': Video.query.count(),
        'images': Image.query.count()
    }
    return render_template('admin/dashboard.html', stats=stats)

# ========== 文章管理 ==========
@app.route('/admin/articles')
@login_required
def admin_articles():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template('admin/articles.html', articles=articles)

@app.route('/admin/articles/new', methods=['GET', 'POST'])
@login_required
def admin_article_new():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        excerpt = request.form.get('excerpt')
        cover_image = request.form.get('cover_image')  # 保存封面图片
        category = request.form.get('category')
        tags = request.form.get('tags')
        status = request.form.get('status', 'published')

        slug = generate_slug(title, Article)

        article = Article(
            title=title,
            slug=slug,
            content=content,
            excerpt=excerpt,
            cover_image=cover_image,  # 保存封面图片
            category=category,
            tags=tags,
            status=status
        )

        # 调试信息
        print(f"🔍 DEBUG: 创建文章，封面图片 - {cover_image}")

        db.session.add(article)
        db.session.commit()
        flash('文章创建成功', 'success')
        return redirect(url_for('admin_articles'))

    return render_template('admin/article_edit.html')

@app.route('/admin/articles/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def admin_article_edit(id):
    article = Article.query.get_or_404(id)
    if request.method == 'POST':
        article.title = request.form.get('title')
        article.content = request.form.get('content')
        article.excerpt = request.form.get('excerpt')
        article.cover_image = request.form.get('cover_image')  # 保存封面图片
        article.category = request.form.get('category')
        article.tags = request.form.get('tags')
        article.status = request.form.get('status', 'published')
        article.updated_at = datetime.utcnow()

        # 调试信息
        print(f"🔍 DEBUG: 保存封面图片 - {article.cover_image}")

        db.session.commit()
        flash('文章更新成功', 'success')
        return redirect(url_for('admin_articles'))

    return render_template('admin/article_edit.html', article=article)

@app.route('/admin/articles/<int:id>/delete', methods=['POST'])
@login_required
def admin_article_delete(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash('文章删除成功', 'success')
    return redirect(url_for('admin_articles'))

# ========== 视频管理 ==========
@app.route('/admin/videos')
@login_required
def admin_videos():
    videos = Video.query.order_by(Video.created_at.desc()).all()
    return render_template('admin/videos.html', videos=videos)

@app.route('/admin/videos/new', methods=['GET', 'POST'])
@login_required
def admin_video_new():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        video_url = request.form.get('video_url')
        category = request.form.get('category')
        tags = request.form.get('tags')
        status = request.form.get('status', 'published')

        slug = generate_slug(title, Video)

        video = Video(
            title=title,
            slug=slug,
            description=description,
            video_url=video_url,
            category=category,
            tags=tags,
            status=status
        )

        db.session.add(video)
        db.session.commit()
        flash('视频创建成功', 'success')
        return redirect(url_for('admin_videos'))

    return render_template('admin/video_edit.html')

@app.route('/admin/videos/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def admin_video_edit(id):
    video = Video.query.get_or_404(id)
    if request.method == 'POST':
        video.title = request.form.get('title')
        video.description = request.form.get('description')
        video.video_url = request.form.get('video_url')
        video.category = request.form.get('category')
        video.tags = request.form.get('tags')
        video.status = request.form.get('status', 'published')
        video.updated_at = datetime.utcnow()

        db.session.commit()
        flash('视频更新成功', 'success')
        return redirect(url_for('admin_videos'))

    return render_template('admin/video_edit.html', video=video)

@app.route('/admin/videos/<int:id>/delete', methods=['POST'])
@login_required
def admin_video_delete(id):
    video = Video.query.get_or_404(id)
    db.session.delete(video)
    db.session.commit()
    flash('视频删除成功', 'success')
    return redirect(url_for('admin_videos'))

# ========== 图片管理 ==========
@app.route('/admin/images')
@login_required
def admin_images():
    images = Image.query.order_by(Image.created_at.desc()).all()
    return render_template('admin/images.html', images=images)

@app.route('/admin/images/upload', methods=['GET', 'POST'])
@login_required
def admin_image_upload():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        category = request.form.get('category')
        tags = request.form.get('tags')
        status = request.form.get('status', 'published')

        # 检查是否有文件
        if 'image' not in request.files:
            flash('没有选择文件', 'error')
            return redirect(request.url)

        file = request.files['image']
        if file.filename == '':
            flash('没有选择文件', 'error')
            return redirect(request.url)

        if file:
            # 验证文件扩展名
            if not allowed_file(file.filename, 'images'):
                flash('不支持的文件格式！仅支持: png, jpg, jpeg, gif, bmp, webp, svg', 'error')
                return redirect(request.url)

            # 检查文件大小
            file.seek(0, os.SEEK_END)
            file_size = file.tell()
            file.seek(0)

            if file_size > app.config['MAX_CONTENT_LENGTH']:
                max_size_mb = app.config['MAX_CONTENT_LENGTH'] // (1024 * 1024)
                flash(f'文件过大！最大允许 {max_size_mb}MB', 'error')
                return redirect(request.url)

            try:
                filename = secure_filename(file.filename)
                unique_filename = f"{uuid.uuid4()}_{filename}"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'images', unique_filename)
                file.save(file_path)

                # 验证文件类型
                if not validate_file_type(file_path, 'image'):
                    os.remove(file_path)  # 删除无效文件
                    flash('无效的图片文件！', 'error')
                    return redirect(request.url)

                # 获取图片尺寸
                try:
                    from PIL import Image as PILImage
                    with PILImage.open(file_path) as img:
                        width, height = img.size
                except:
                    width, height = None, None

                # 获取实际文件大小
                actual_file_size = os.path.getsize(file_path)
                slug = generate_slug(title, Image)

                image = Image(
                    title=title,
                    slug=slug,
                    description=description,
                    filename=filename,
                    filepath=f'uploads/images/{unique_filename}',
                    file_size=actual_file_size,
                    mime_type=file.content_type,
                    width=width,
                    height=height,
                    category=category,
                    tags=tags,
                    status=status
                )

                db.session.add(image)
                db.session.commit()
                flash('图片上传成功', 'success')
                return redirect(url_for('admin_images'))

            except Exception as e:
                flash(f'上传失败: {str(e)}', 'error')
                return redirect(request.url)

    return render_template('admin/image_upload.html')

@app.route('/admin/images/<int:id>/delete', methods=['POST'])
@login_required
def admin_image_delete(id):
    image = Image.query.get_or_404(id)
    # 删除物理文件
    file_path = os.path.join(image.filepath)
    if os.path.exists(file_path):
        os.remove(file_path)
    db.session.delete(image)
    db.session.commit()
    flash('图片删除成功', 'success')
    return redirect(url_for('admin_images'))

# ========== API接口 ==========

# 获取文章API
@app.route('/api/articles')
def api_articles():
    articles = Article.query.filter_by(status='published').order_by(Article.created_at.desc()).all()
    return jsonify([article.to_dict() for article in articles])

@app.route('/api/articles/<slug>')
def api_article(slug):
    article = Article.query.filter_by(slug=slug, status='published').first_or_404()
    return jsonify(article.to_dict())

# 获取视频API
@app.route('/api/videos')
def api_videos():
    videos = Video.query.filter_by(status='published').order_by(Video.created_at.desc()).all()
    return jsonify([video.to_dict() for video in videos])

@app.route('/api/videos/<slug>')
def api_video(slug):
    video = Video.query.filter_by(slug=slug, status='published').first_or_404()
    return jsonify(video.to_dict())

# 获取图片API
@app.route('/api/images')
def api_images():
    images = Image.query.filter_by(status='published').order_by(Image.created_at.desc()).all()
    return jsonify([image.to_dict() for image in images])

@app.route('/api/images/<slug>')
def api_image(slug):
    image = Image.query.filter_by(slug=slug, status='published').first_or_404()
    return jsonify(image.to_dict())

# ==================== 动态页面路由 ====================

@app.route('/api/dynamic-pages')
def api_dynamic_pages():
    """获取所有动态页面列表"""
    pages = DynamicPage.query.filter_by(status='published').order_by(DynamicPage.created_at.desc()).all()
    return jsonify([page.to_dict() for page in pages])

@app.route('/api/dynamic-pages/<slug>')
def api_dynamic_page(slug):
    """获取特定动态页面"""
    page = DynamicPage.query.filter_by(slug=slug, status='published').first_or_404()
    page.views += 1
    db.session.commit()
    return jsonify(page.to_dict())

@app.route('/api/dynamic-pages/<slug>/blocks')
def api_dynamic_page_blocks(slug):
    """获取动态页面的内容块"""
    page = DynamicPage.query.filter_by(slug=slug, status='published').first_or_404()
    blocks = ContentBlock.query.filter_by(page_id=page.id, visible=True).order_by(ContentBlock.sort_order).all()
    return jsonify([block.to_dict() for block in blocks])

# ==================== 管理后台路由 ====================

@app.route('/admin/dynamic-pages')
@login_required
def admin_dynamic_pages():
    """动态页面列表"""
    pages = DynamicPage.query.order_by(DynamicPage.created_at.desc()).all()
    return render_template('admin/dynamic_pages.html', pages=pages)

@app.route('/admin/dynamic-pages/new', methods=['GET', 'POST'])
@login_required
def admin_dynamic_page_new():
    """创建新动态页面"""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        slug = request.form.get('slug', '').strip()
        description = request.form.get('description', '').strip()
        cover_image = request.form.get('cover_image', '').strip()

        if not title or not slug:
            flash('标题和别名不能为空', 'error')
            return render_template('admin/dynamic_page_edit.html')

        # 检查slug是否已存在
        if DynamicPage.query.filter_by(slug=slug).first():
            flash('别名已存在，请使用其他别名', 'error')
            return render_template('admin/dynamic_page_edit.html')

        page = DynamicPage(
            title=title,
            slug=slug,
            description=description,
            cover_image=cover_image
        )
        db.session.add(page)
        db.session.commit()
        flash('页面创建成功', 'success')
        return redirect(url_for('admin_dynamic_page_edit', id=page.id))

    return render_template('admin/dynamic_page_edit.html')

@app.route('/admin/dynamic-pages/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def admin_dynamic_page_edit(id):
    """编辑动态页面"""
    page = DynamicPage.query.get_or_404(id)

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        slug = request.form.get('slug', '').strip()
        description = request.form.get('description', '').strip()
        cover_image = request.form.get('cover_image', '').strip()

        if not title or not slug:
            flash('标题和别名不能为空', 'error')
            return render_template('admin/dynamic_page_edit.html', page=page)

        # 检查slug是否已存在（排除当前页面）
        existing = DynamicPage.query.filter_by(slug=slug).first()
        if existing and existing.id != page.id:
            flash('别名已存在，请使用其他别名', 'error')
            return render_template('admin/dynamic_page_edit.html', page=page)

        page.title = title
        page.slug = slug
        page.description = description
        page.cover_image = cover_image

        db.session.commit()
        flash('页面更新成功', 'success')
        return redirect(url_for('admin_dynamic_pages'))

    return render_template('admin/dynamic_page_edit.html', page=page)

@app.route('/admin/dynamic-pages/<int:id>/delete', methods=['POST'])
@login_required
def admin_dynamic_page_delete(id):
    """删除动态页面"""
    page = DynamicPage.query.get_or_404(id)
    db.session.delete(page)
    db.session.commit()
    flash('页面已删除', 'success')
    return redirect(url_for('admin_dynamic_pages'))

@app.route('/admin/dynamic-pages/<int:id>/grid-editor')
@login_required
def admin_dynamic_page_grid_editor(id):
    """网格页面编辑器"""
    page = DynamicPage.query.get_or_404(id)
    return render_template('admin/grid_page_editor.html', page=page)

@app.route('/admin/dynamic-pages/<int:id>/editor')
@login_required
def admin_dynamic_page_editor(id):
    """动态页面拖拽编辑器"""
    page = DynamicPage.query.get_or_404(id)
    return render_template('admin/dynamic_page_editor.html', page=page)

# ==================== 网格布局API ====================

@app.route('/api/admin/pages/<int:page_id>/grid-layout', methods=['GET'])
@login_required
def api_get_grid_layout(page_id):
    """获取页面的网格布局"""
    page = DynamicPage.query.get_or_404(page_id)
    return jsonify({
        'page_id': page_id,
        'elements': page.blocks if hasattr(page, 'blocks') else []
    })

@app.route('/api/admin/pages/<int:page_id>/grid-layout', methods=['POST'])
@login_required
def api_save_grid_layout(page_id):
    """保存页面的网格布局"""
    page = DynamicPage.query.get_or_404(page_id)
    data = request.get_json()

    # 删除旧的布局
    ContentBlock.query.filter_by(page_id=page_id).delete()

    # 保存新布局
    elements = data.get('elements', [])
    for i, element in enumerate(elements):
        block = ContentBlock(
            page_id=page_id,
            block_type=element.get('type', 'text'),
            sort_order=i,
            visible=True
        )
        block.set_content(element.get('content', {}))
        block.set_style(element.get('style', {}))
        db.session.add(block)

    db.session.commit()
    return jsonify({'message': '网格布局已保存'})

@app.route('/api/dynamic-pages/<slug>/blocks', methods=['GET'])
def api_get_dynamic_page_blocks(slug):
    """获取动态页面的内容块（前台API）"""
    page = DynamicPage.query.filter_by(slug=slug, status='published').first_or_404()
    blocks = ContentBlock.query.filter_by(page_id=page.id, visible=True).order_by(ContentBlock.sort_order).all()
    return jsonify([block.to_dict() for block in blocks])

# ==================== 首页配置管理 ====================

@app.route('/admin/homepage-config')
@login_required
def admin_homepage_config():
    """首页配置管理页面"""
    config = HomepageConfig.query.filter_by(name='default').first()
    return render_template('admin/homepage_config.html', config=config)

# ==================== 首页配置API ====================

@app.route('/api/admin/homepage-config', methods=['GET'])
@login_required
def api_get_homepage_config():
    """获取首页配置"""
    config = HomepageConfig.query.filter_by(name='default').first()
    if not config:
        return jsonify({'error': 'Config not found'}), 404
    return jsonify(config.to_dict())

@app.route('/api/admin/homepage-config', methods=['PUT'])
@login_required
def api_update_homepage_config():
    """更新首页配置"""
    config = HomepageConfig.query.filter_by(name='default').first()
    if not config:
        return jsonify({'error': 'Config not found'}), 404

    data = request.get_json()

    # 更新配置数据
    if 'config' in data:
        config.set_config(data['config'])

    # 更新是否启用
    if 'enabled' in data:
        config.enabled = data['enabled']

    db.session.commit()
    return jsonify(config.to_dict())

# ==================== 菜单管理 ====================

@app.route('/admin/menu-management')
@login_required
def admin_menu_management():
    """菜单管理页面"""
    return render_template('admin/menu_management.html')

# ==================== 菜单管理API ====================

@app.route('/api/admin/menu-items', methods=['GET'])
@login_required
def api_get_menu_items():
    """获取所有菜单项（管理后台）"""
    # 获取顶级菜单项（parent_id为None），并预加载子菜单
    menu_items = MenuItem.query.filter_by(parent_id=None).order_by(MenuItem.order).all()
    return jsonify({
        'success': True,
        'data': [item.to_dict() for item in menu_items]
    })

@app.route('/api/admin/menu-items', methods=['POST'])
@login_required
def api_create_menu_item():
    """创建新菜单项"""
    data = request.get_json()

    # 验证必填字段
    if not data.get('label') or not data.get('url'):
        return jsonify({'error': 'Label and URL are required'}), 400

    # 获取当前最大排序号
    max_order = db.session.query(db.func.max(MenuItem.order)).filter_by(parent_id=data.get('parent_id')).scalar() or 0

    menu_item = MenuItem(
        label=data['label'],
        url=data['url'],
        icon=data.get('icon'),
        order=max_order + 1,
        visible=data.get('visible', True),
        parent_id=data.get('parent_id')
    )

    db.session.add(menu_item)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': menu_item.to_dict()
    }), 201

@app.route('/api/admin/menu-items/<int:menu_id>', methods=['PUT'])
@login_required
def api_update_menu_item(menu_id):
    """更新菜单项"""
    menu_item = MenuItem.query.get_or_404(menu_id)
    data = request.get_json()

    # 更新字段
    if 'label' in data:
        menu_item.label = data['label']
    if 'url' in data:
        menu_item.url = data['url']
    if 'icon' in data:
        menu_item.icon = data['icon']
    if 'visible' in data:
        menu_item.visible = data['visible']
    if 'parent_id' in data:
        # 防止设置为自己或自己的子菜单为父菜单
        if data['parent_id'] == menu_item.id:
            return jsonify({'error': 'Cannot set menu as its own parent'}), 400
        if data['parent_id']:
            # 检查是否会创建循环引用
            parent = MenuItem.query.get(data['parent_id'])
            if parent and is_descendant(parent, menu_item.id):
                return jsonify({'error': 'Cannot create circular reference'}), 400
        menu_item.parent_id = data['parent_id']
    if 'order' in data:
        menu_item.order = data['order']

    db.session.commit()

    return jsonify({
        'success': True,
        'data': menu_item.to_dict()
    })

@app.route('/api/admin/menu-items/<int:menu_id>', methods=['DELETE'])
@login_required
def api_delete_menu_item(menu_id):
    """删除菜单项"""
    menu_item = MenuItem.query.get_or_404(menu_id)
    db.session.delete(menu_item)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Menu item deleted successfully'
    })

@app.route('/api/admin/menu-items/reorder', methods=['POST'])
@login_required
def api_reorder_menu_items():
    """批量重新排序菜单项"""
    data = request.get_json()
    items = data.get('items', [])

    for item_data in items:
        menu_item = MenuItem.query.get(item_data['id'])
        if menu_item:
            menu_item.order = item_data['order']

    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Menu items reordered successfully'
    })

@app.route('/api/menu-items', methods=['GET'])
def api_get_visible_menu_items():
    """获取可见菜单项（前端渲染用）"""
    # 只获取顶级可见菜单项
    menu_items = MenuItem.query.filter_by(parent_id=None, visible=True).order_by(MenuItem.order).all()
    return jsonify([item.to_dict() for item in menu_items])

def is_descendant(menu_item, ancestor_id):
    """检查menu_item是否是ancestor_id的子孙菜单"""
    if menu_item.id == ancestor_id:
        return True
    if not menu_item.parent:
        return False
    return is_descendant(menu_item.parent, ancestor_id)

# ==================== 内容块管理API ====================

@app.route('/api/admin/pages/<int:page_id>/blocks', methods=['GET'])
@login_required
def api_get_blocks(page_id):
    """获取页面的所有内容块"""
    blocks = ContentBlock.query.filter_by(page_id=page_id).order_by(ContentBlock.sort_order).all()
    return jsonify([block.to_dict() for block in blocks])

@app.route('/api/admin/pages/<int:page_id>/blocks', methods=['POST'])
@login_required
def api_create_block(page_id):
    """创建新的内容块"""
    page = DynamicPage.query.get_or_404(page_id)
    data = request.get_json()

    # 获取当前最大排序号
    max_order = db.session.query(db.func.max(ContentBlock.sort_order)).filter_by(page_id=page_id).scalar() or 0

    block = ContentBlock(
        page_id=page_id,
        block_type=data.get('block_type', 'text'),
        sort_order=max_order + 1,
        visible=data.get('visible', True)
    )

    # 设置内容和样式
    if 'content' in data:
        block.set_content(data['content'])
    if 'style' in data:
        block.set_style(data['style'])

    db.session.add(block)
    db.session.commit()

    return jsonify(block.to_dict())

@app.route('/api/admin/blocks/<int:block_id>', methods=['PUT'])
@login_required
def api_update_block(block_id):
    """更新内容块"""
    block = ContentBlock.query.get_or_404(block_id)
    data = request.get_json()

    if 'block_type' in data:
        block.block_type = data['block_type']
    if 'content' in data:
        block.set_content(data['content'])
    if 'style' in data:
        block.set_style(data['style'])
    if 'sort_order' in data:
        block.sort_order = data['sort_order']
    if 'visible' in data:
        block.visible = data['visible']

    db.session.commit()
    return jsonify(block.to_dict())

@app.route('/api/admin/blocks/<int:block_id>', methods=['DELETE'])
@login_required
def api_delete_block(block_id):
    """删除内容块"""
    block = ContentBlock.query.get_or_404(block_id)
    db.session.delete(block)
    db.session.commit()
    return jsonify({'message': 'Block deleted successfully'})

@app.route('/api/admin/pages/<int:page_id>/blocks/reorder', methods=['POST'])
@login_required
def api_reorder_blocks(page_id):
    """重新排序内容块"""
    data = request.get_json()
    block_orders = data.get('block_orders', [])

    for i, block_id in enumerate(block_orders):
        block = ContentBlock.query.filter_by(id=block_id, page_id=page_id).first()
        if block:
            block.sort_order = i

    db.session.commit()
    return jsonify({'message': 'Blocks reordered successfully'})

# ==================== 前台页面路由 ====================

@app.route('/page/<slug>')
def dynamic_page_view(slug):
    """动态页面前台显示"""
    page = DynamicPage.query.filter_by(slug=slug, status='published').first_or_404()
    page.views += 1
    db.session.commit()

    # 检查是否有网格布局
    has_grid_layout = ContentBlock.query.filter_by(page_id=page.id).count() > 0

    if has_grid_layout:
        return render_template('grid_page_display.html', page=page)
    else:
        return render_template('dynamic_page.html', page=page)

# JavaScript功能测试路由
@app.route('/test-js')
def test_js():
    """测试JavaScript功能的页面"""
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript 测试</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>🎉 封面图片功能 - JavaScript测试</h1>
        <p class="lead">此页面用于测试后台管理界面的JavaScript功能</p>

        <div class="mt-4">
            <button type="button" class="btn btn-outline-primary btn-lg" onclick="showCoverImagePicker()">
                <i class="fas fa-images me-2"></i>从图片库选择
            </button>
            <button type="button" class="btn btn-outline-secondary btn-lg" onclick="uploadNewCoverImage()">
                <i class="fas fa-upload me-2"></i>上传新封面
            </button>
        </div>

        <div id="output" class="mt-4 alert alert-info" style="display:none;"></div>
        <div id="status" class="mt-2"></div>
    </div>

    <script>
        console.log('🚀 JavaScript测试脚本加载中...');

        // 测试函数1：图片库选择
        function showCoverImagePicker() {
            console.log('✅ showCoverImagePicker 被调用!');
            const output = document.getElementById('output');
            const status = document.getElementById('status');
            output.style.display = 'block';
            output.innerHTML = '<h4>🔄 正在加载图片库...</h4><div class="spinner-border spinner-border-sm"></div>';

            fetch('/api/images')
                .then(response => {
                    if (!response.ok) throw new Error('网络响应异常');
                    return response.json();
                })
                .then(images => {
                    console.log('✅ 图片加载成功:', images);
                    let html = '<h4>✅ API调用成功!</h4><p>找到 <strong>' + images.length + '</strong> 张图片:</p><div class="row">';
                    images.forEach(img => {
                        html += '<div class="col-md-4 mb-3"><div class="card"><img src="/static/' + img.filepath + '" class="card-img-top" style="height:150px;object-fit:cover;"><div class="card-body"><h6 class="card-title">' + img.title + '</h6></div></div></div>';
                    });
                    html += '</div>';
                    output.innerHTML = html;
                    status.innerHTML = '<div class="alert alert-success mt-3">✅ 所有JavaScript功能正常工作！</div>';
                })
                .catch(error => {
                    console.error('❌ API调用失败:', error);
                    output.innerHTML = '<h4>❌ API调用失败</h4><p>' + error.message + '</p>';
                    status.innerHTML = '<div class="alert alert-danger mt-3">❌ 请检查网络连接和API状态</div>';
                });
        }

        // 测试函数2：上传新封面
        function uploadNewCoverImage() {
            console.log('✅ uploadNewCoverImage 被调用!');
            const output = document.getElementById('output');
            const status = document.getElementById('status');
            output.style.display = 'block';
            output.innerHTML = '<h4>📁 请选择图片文件</h4><p>点击确定打开文件选择对话框...</p>';

            const input = document.createElement('input');
            input.type = 'file';
            input.accept = 'image/*';
            input.onchange = function(e) {
                const file = e.target.files[0];
                if (file) {
                    console.log('✅ 文件已选择:', file.name, file.size);
                    output.innerHTML = '<h4>✅ 文件选择成功!</h4><p><strong>文件名:</strong> ' + file.name + '<br><strong>大小:</strong> ' + (file.size/1024).toFixed(2) + ' KB<br><strong>类型:</strong> ' + file.type + '</p>';
                    status.innerHTML = '<div class="alert alert-success mt-3">✅ 文件选择功能正常！</div>';
                }
            };
            input.click();
        }

        console.log('✅ 脚本加载完成! 准备就绪!');
        document.getElementById('output').innerHTML = '<h4>🚀 JavaScript测试页面已就绪</h4><p>点击上方按钮测试功能</p>';
        document.getElementById('output').style.display = 'block';
    </script>
</body>
</html>
'''

# 创建数据库表
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
