# 设计文档：菜单管理系统

## 架构设计

### 1. 数据库模型设计

#### MenuItem 模型字段

```python
class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(50), nullable=False)  # 菜单显示名称
    url = db.Column(db.String(200), nullable=False)   # 链接地址
    icon = db.Column(db.String(50))                   # Font Awesome图标类
    order = db.Column(db.Integer, default=0)          # 排序顺序
    visible = db.Column(db.Boolean, default=True)     # 是否显示
    parent_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'))  # 父菜单ID
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 自关联，支持多级菜单
    children = db.relationship('MenuItem',
                               backref=db.backref('parent', remote_side=[id]),
                               cascade='all, delete-orphan')
```

#### 关系设计

- **自关联**：每个菜单项可以有子菜单
- **级联删除**：删除父菜单时自动删除子菜单
- **排序**：通过 `order` 字段控制显示顺序

### 2. API设计

#### 菜单管理API端点

```
GET  /api/admin/menu-items           # 获取所有菜单项（树形结构）
POST /api/admin/menu-items           # 创建新菜单项
PUT  /api/admin/menu-items/<id>      # 更新菜单项
DELETE /api/admin/menu-items/<id>    # 删除菜单项
POST /api/admin/menu-items/reorder   # 批量重新排序
```

#### 菜单渲染API端点

```
GET /api/menu-items                 # 获取前端渲染用菜单（仅可见项）
```

### 3. 前端设计

#### 管理界面页面

**URL：** `/admin/menu-management`

**功能：**
- 菜单项列表（树形展示）
- 添加新菜单项
- 编辑菜单项
- 删除菜单项
- 拖拽排序
- 启用/禁用切换

**UI组件：**
- 树形菜单组件
- 拖拽排序（SortableJS）
- 图标选择器（Font Awesome）
- 父菜单选择下拉框
- 确认删除对话框

#### 前端模板修改

**文件：** `templates/base.html`

**修改内容：**
```html
<!-- 原有硬编码菜单 -->
<ul class="navbar-nav me-auto">
    <!-- 替换为动态菜单 -->
    {% for item in menu_items %}
    <li class="nav-item {{ 'dropdown' if item.children }}">
        {% if item.children %}
        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
            {% if item.icon %}<i class="{{ item.icon }} me-1"></i>{% endif %}
            {{ item.label }}
        </a>
        <ul class="dropdown-menu">
            {% for child in item.children %}
            <li><a class="dropdown-item" href="{{ item.url }}">
                {% if child.icon %}<i class="{{ child.icon }} me-1"></i>{% endif %}
                {{ child.label }}
            </a></li>
            {% endfor %}
        </ul>
        {% else %}
        <a class="nav-link" href="{{ item.url }}">
            {% if item.icon %}<i class="{{ item.icon }} me-1"></i>{% endif %}
            {{ item.label }}
        </a>
        {% endif %}
    </li>
    {% endfor %}
</ul>
```

### 4. 默认数据设计

创建默认菜单项（应用启动时初始化）：

```python
DEFAULT_MENU_ITEMS = [
    {'label': '首页', 'url': '/', 'icon': 'fas fa-home', 'order': 0},
    {'label': '文章', 'url': '/articles', 'icon': 'fas fa-newspaper', 'order': 1},
    {'label': '视频', 'url': '/videos', 'icon': 'fas fa-video', 'order': 2},
    {'label': '图片', 'url': '/images', 'icon': 'fas fa-images', 'order': 3},
]
```

### 5. 技术栈

- **后端**：Flask + SQLAlchemy
- **前端**：Bootstrap 5 + Font Awesome 6
- **拖拽排序**：SortableJS
- **图标选择**：Font Awesome类名直接输入

### 6. 数据迁移策略

1. **首次运行**：
   - 创建 `menu_items` 表
   - 插入默认菜单数据

2. **升级场景**：
   - 检查表是否存在
   - 如不存在则创建并插入默认数据

### 7. 性能考虑

- **缓存**：菜单数据可缓存，减少数据库查询
- **索引**：`parent_id` 和 `order` 字段添加索引
- **查询优化**：前端渲染时使用预加载（joinedload）

### 8. 安全考虑

- **权限控制**：菜单管理仅限管理员访问
- **URL验证**：验证菜单URL安全性
- **XSS防护**：对用户输入进行转义

### 9. 测试策略

- **单元测试**：模型方法、API端点
- **集成测试**：前端表单提交、数据渲染
- **手动测试**：完整用户流程验证

## 实施优先级

### 阶段1：核心功能（MVP）
1. 创建MenuItem模型
2. 实现基本CRUD API
3. 开发管理界面
4. 修改前端模板
5. 创建默认数据

### 阶段2：增强功能
1. 拖拽排序
2. 图标选择器
3. 菜单验证

### 阶段3：高级功能（未来）
1. 多级下拉菜单
2. 菜单分组
3. 条件显示（基于用户权限）
4. 菜单徽章/计数器

## 兼容性说明

- **向后兼容**：现有功能不受影响
- **数据库**：添加新表，不修改现有表
- **模板**：保留现有导航样式
- **API**：新增API，不破坏现有API

---

**版本：** 1.0
**最后更新：** 2025-10-29
