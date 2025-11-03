from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import json

db = SQLAlchemy()

class Article(db.Model):
    """文章模型"""
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.String(500))
    cover_image = db.Column(db.String(200))
    category = db.Column(db.String(50))
    tags = db.Column(db.String(200))  # 逗号分隔的标签
    author = db.Column(db.String(100), default='Admin')
    status = db.Column(db.String(20), default='published')  # published, draft
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Article {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'content': self.content,
            'excerpt': self.excerpt,
            'cover_image': self.cover_image,
            'category': self.category,
            'tags': self.tags.split(',') if self.tags else [],
            'author': self.author,
            'status': self.status,
            'views': self.views,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Video(db.Model):
    """视频模型"""
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.Text)
    video_url = db.Column(db.String(500), nullable=False)  # 视频文件路径或外链
    thumbnail = db.Column(db.String(200))  # 缩略图
    duration = db.Column(db.Integer)  # 时长（秒）
    category = db.Column(db.String(50))
    tags = db.Column(db.String(200))  # 逗号分隔的标签
    author = db.Column(db.String(100), default='Admin')
    status = db.Column(db.String(20), default='published')  # published, draft
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Video {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'description': self.description,
            'video_url': self.video_url,
            'thumbnail': self.thumbnail,
            'duration': self.duration,
            'category': self.category,
            'tags': self.tags.split(',') if self.tags else [],
            'author': self.author,
            'status': self.status,
            'views': self.views,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Image(db.Model):
    """图片模型"""
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.Text)
    filename = db.Column(db.String(200), nullable=False)  # 文件名
    filepath = db.Column(db.String(500), nullable=False)  # 文件路径
    thumbnail = db.Column(db.String(200))  # 缩略图路径
    file_size = db.Column(db.Integer)  # 文件大小（字节）
    mime_type = db.Column(db.String(100))  # MIME类型
    width = db.Column(db.Integer)  # 宽度
    height = db.Column(db.Integer)  # 高度
    category = db.Column(db.String(50))
    tags = db.Column(db.String(200))  # 逗号分隔的标签
    author = db.Column(db.String(100), default='Admin')
    status = db.Column(db.String(20), default='published')  # published, draft
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Image {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'description': self.description,
            'filename': self.filename,
            'filepath': self.filepath,
            'thumbnail': self.thumbnail,
            'file_size': self.file_size,
            'mime_type': self.mime_type,
            'width': self.width,
            'height': self.height,
            'category': self.category,
            'tags': self.tags.split(',') if self.tags else [],
            'author': self.author,
            'status': self.status,
            'views': self.views,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class DynamicPage(db.Model):
    """动态页面模型 - 支持拖拽式编辑器"""
    __tablename__ = 'dynamic_pages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.String(500))  # 页面描述
    cover_image = db.Column(db.String(200))  # 封面图
    author = db.Column(db.String(100), default='Admin')
    status = db.Column(db.String(20), default='published')  # published, draft
    views = db.Column(db.Integer, default=0)
    show_menu_navigation = db.Column(db.Boolean, default=True)  # 是否显示顶部菜单导航
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关联的内容块
    blocks = db.relationship('ContentBlock', backref='page', cascade='all, delete-orphan', order_by='ContentBlock.sort_order')

    def __repr__(self):
        return f'<DynamicPage {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'description': self.description,
            'cover_image': self.cover_image,
            'author': self.author,
            'status': self.status,
            'views': self.views,
            'show_menu_navigation': self.show_menu_navigation,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'blocks': [block.to_dict() for block in self.blocks]
        }

class ContentBlock(db.Model):
    """内容块模型 - 可拖拽的页面元素"""
    __tablename__ = 'content_blocks'

    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('dynamic_pages.id'), nullable=False)

    # 块类型: text(文本), image(图片), video(视频), article(文章引用), divider(分隔线), quote(引用), code(代码)
    block_type = db.Column(db.String(20), nullable=False)

    # 内容数据 (JSON格式存储)
    content_data = db.Column(db.Text)  # JSON字符串

    # 样式设置 (JSON格式存储)
    style_data = db.Column(db.Text)  # JSON字符串

    # 排序顺序
    sort_order = db.Column(db.Integer, default=0)

    # 是否可见
    visible = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<ContentBlock {self.block_type} #{self.id}>'

    def get_content(self):
        """获取解析后的内容数据"""
        if self.content_data:
            try:
                return json.loads(self.content_data)
            except json.JSONDecodeError:
                return {}
        return {}

    def set_content(self, data):
        """设置内容数据"""
        self.content_data = json.dumps(data, ensure_ascii=False)

    def get_style(self):
        """获取解析后的样式数据"""
        if self.style_data:
            try:
                return json.loads(self.style_data)
            except json.JSONDecodeError:
                return {}
        return {}

    def set_style(self, data):
        """设置样式数据"""
        self.style_data = json.dumps(data, ensure_ascii=False)

    def to_dict(self):
        return {
            'id': self.id,
            'page_id': self.page_id,
            'block_type': self.block_type,
            'content': self.get_content(),
            'style': self.get_style(),
            'sort_order': self.sort_order,
            'visible': self.visible,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class HomepageConfig(db.Model):
    """首页配置模型 - 支持可定制布局"""
    __tablename__ = 'homepage_configs'

    id = db.Column(db.Integer, primary_key=True)

    # 配置名称
    name = db.Column(db.String(100), nullable=False, unique=True)

    # 配置数据 (JSON格式存储布局信息)
    config_data = db.Column(db.Text)

    # 是否启用
    enabled = db.Column(db.Boolean, default=True)

    # 创建和更新时间
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<HomepageConfig {self.name}>'

    def get_config(self):
        """获取解析后的配置数据"""
        if self.config_data:
            try:
                return json.loads(self.config_data)
            except json.JSONDecodeError:
                return {}
        return {}

    def set_config(self, data):
        """设置配置数据"""
        self.config_data = json.dumps(data, ensure_ascii=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'config': self.get_config(),
            'enabled': self.enabled,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class MenuItem(db.Model):
    """菜单项模型 - 支持动态菜单管理"""
    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)

    # 菜单显示名称
    label = db.Column(db.String(50), nullable=False)

    # 链接地址
    url = db.Column(db.String(200), nullable=False)

    # Font Awesome图标类名
    icon = db.Column(db.String(50))

    # 排序顺序
    order = db.Column(db.Integer, default=0)

    # 是否可见
    visible = db.Column(db.Boolean, default=True)

    # 父菜单ID (自关联)
    parent_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'))

    # 创建和更新时间
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 自关联关系 - 支持多级菜单
    children = db.relationship('MenuItem',
                               backref=db.backref('parent', remote_side=[id]),
                               cascade='all, delete-orphan',
                               order_by='MenuItem.order')

    def __repr__(self):
        return f'<MenuItem {self.label}>'

    def to_dict(self):
        return {
            'id': self.id,
            'label': self.label,
            'url': self.url,
            'icon': self.icon,
            'order': self.order,
            'visible': self.visible,
            'parent_id': self.parent_id,
            'children': [child.to_dict() for child in self.children],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Link(db.Model):
    """链接模型 - 用于首页链接展示"""
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)

    # 链接标题
    title = db.Column(db.String(100), nullable=False)

    # 链接地址
    url = db.Column(db.String(500), nullable=False)

    # 链接描述
    description = db.Column(db.Text)

    # 链接图标
    icon = db.Column(db.String(50))  # Font Awesome图标类名

    # 链接图片
    image = db.Column(db.String(200))  # 链接图片路径

    # 排序顺序
    sort_order = db.Column(db.Integer, default=0)

    # 是否可见
    visible = db.Column(db.Boolean, default=True)

    # 链接分类
    category = db.Column(db.String(50))

    # 作者
    author = db.Column(db.String(100), default='Admin')

    # 状态
    status = db.Column(db.String(20), default='published')  # published, draft

    # 创建和更新时间
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Link {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'description': self.description,
            'icon': self.icon,
            'image': self.image,
            'sort_order': self.sort_order,
            'visible': self.visible,
            'category': self.category,
            'author': self.author,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class User(db.Model):
    """用户模型 - 支持多用户管理和权限控制"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # 用户名（唯一）
    username = db.Column(db.String(50), nullable=False, unique=True)

    # 密码哈希
    password_hash = db.Column(db.String(255), nullable=False)

    # 电子邮件（可选）
    email = db.Column(db.String(100), unique=True)

    # 显示名称
    display_name = db.Column(db.String(50), nullable=False)

    # 角色：admin（管理员）、editor（编辑）、viewer（查看者）
    role = db.Column(db.String(20), default='viewer', nullable=False)

    # 权限：JSON格式存储详细权限
    # 例如：{"articles": {"read": true, "write": true, "delete": false}}
    permissions = db.Column(db.Text)

    # 是否激活
    active = db.Column(db.Boolean, default=True)

    # 最后登录时间
    last_login = db.Column(db.DateTime)

    # 创建和更新时间
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        """设置密码（自动生成哈希）"""
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """验证密码"""
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)

    def get_permissions(self):
        """获取解析后的权限数据"""
        if self.permissions:
            try:
                return json.loads(self.permissions)
            except json.JSONDecodeError:
                return {}
        return {}

    def set_permissions(self, data):
        """设置权限数据"""
        self.permissions = json.dumps(data, ensure_ascii=False)

    def is_admin(self):
        """是否为管理员"""
        return self.role == 'admin'

    def is_editor(self):
        """是否为编辑"""
        return self.role == 'editor'

    def has_permission(self, resource, action='read'):
        """检查是否有指定资源的权限"""
        # 管理员拥有所有权限
        if self.role == 'admin':
            return True

        # 查看者无编辑权限
        if self.role == 'viewer' and action != 'read':
            return False

        # 获取权限配置
        permissions = self.get_permissions()

        # 检查具体资源权限
        if resource in permissions:
            resource_perms = permissions[resource]
            if action in resource_perms:
                return resource_perms[action]

        return False

    def to_dict(self):
        """转换为字典（不包含密码哈希）"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'display_name': self.display_name,
            'role': self.role,
            'permissions': self.get_permissions(),
            'active': self.active,
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
