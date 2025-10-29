# 菜单管理功能规范

## ADDED Requirements

### Requirement: MenuItem数据模型创建

**描述：** 系统 SHALL 创建MenuItem数据库模型支持动态菜单管理

**Details:**
- 表名：`menu_items`
- 字段：id, label, url, icon, order, visible, parent_id, created_at, updated_at
- 支持自关联关系（parent-child）
- 支持级联删除
- 添加数据库索引

**Details:**
- 表名：`menu_items`
- 字段：id, label, url, icon, order, visible, parent_id, created_at, updated_at
- 支持自关联关系（parent-child）
- 支持级联删除
- 添加数据库索引

**Implementation Location:**
- 文件：`models.py`
- 类：`MenuItem`

**Validation:**
- 模型能正确创建数据库表
- 关系配置正确
- to_dict()方法返回正确数据格式

#### Scenario: 创建MenuItem模型
**Given** models.py文件
**When** 添加MenuItem类定义
**Then** 数据库表menu_items成功创建
**And** 字段包含所有必要属性
**And** 自关联关系配置正确

---

### Requirement: 默认菜单初始化

**描述：** 应用 SHALL 在首次启动时自动创建默认菜单项

**Details:**
- 默认包含：首页、文章、视频、图片
- 设置合理的显示顺序（0-3）
- 为每个菜单分配Font Awesome图标
- 跳过初始化如果菜单已存在

**Implementation Location:**
- 文件：`app.py`
- 函数：`init_menu_items()`

**Validation:**
- 首次运行后数据库包含4条菜单记录
- 重复启动不会重复创建
- 默认菜单数据正确

#### Scenario: 初始化默认菜单
**Given** 空的menu_items表
**When** 调用init_menu_items()
**Then** 插入4条默认菜单记录
**And** 每个菜单包含label、url、icon、order字段
**And** order字段为0-3连续值

---

### Requirement: 菜单管理API - 获取列表

**描述：** 系统 MUST 提供REST API获取所有菜单项

**Endpoint:**
```
GET /api/admin/menu-items
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "label": "首页",
      "url": "/",
      "icon": "fas fa-home",
      "order": 0,
      "visible": true,
      "parent_id": null,
      "children": []
    }
  ]
}
```

**Implementation Location:**
- 文件：`app.py`
- 路由：`/api/admin/menu-items`

**Validation:**
- 返回所有菜单项（树形结构）
- 按order字段排序
- 包含children字段

#### Scenario: 获取菜单列表
**Given** 管理员请求GET /api/admin/menu-items
**When** API返回菜单数据
**Then** 包含所有菜单项
**And** 按order排序
**And** 树形结构children字段正确

---

### Requirement: 菜单管理API - 创建菜单项

**描述：** 系统 MUST 允许管理员创建新菜单项

**Endpoint:**
```
POST /api/admin/menu-items
```

**Request Body:**
```json
{
  "label": "新菜单",
  "url": "/new-page",
  "icon": "fas fa-star",
  "order": 5,
  "visible": true,
  "parent_id": null
}
```

**Validation Rules:**
- label必填（1-50字符）
- url必填
- order默认为最大值+1
- visible默认为true
- parent_id可选（创建顶级菜单）

**Implementation Location:**
- 文件：`app.py`
- 路由：`/api/admin/menu-items`

**Validation:**
- 成功创建返回201状态
- 失败返回错误信息
- 数据验证正确

#### Scenario: 创建新菜单项
**Given** 管理员发送POST请求
**When** 提交有效的菜单数据
**Then** 返回201状态和菜单ID
**And** 数据库新增一条记录
**And** 默认order为最大值+1

---

### Requirement: 菜单管理API - 更新菜单项

**描述：** 系统 MUST 允许管理员修改现有菜单项

**Endpoint:**
```
PUT /api/admin/menu-items/<id>
```

**Request Body:** 同创建API

**Validation Rules:**
- 菜单项必须存在
- label、url不能为空
- parent_id不能设置为自己的子菜单
- 不能创建循环引用

**Implementation Location:**
- 文件：`app.py`
- 路由：`/api/admin/menu-items/<id>`

**Validation:**
- 更新成功返回200状态
- 不存在的ID返回404
- 循环引用检测

#### Scenario: 更新菜单项
**Given** 管理员发送PUT请求
**When** 修改菜单label和url
**Then** 返回200状态
**And** 数据库记录更新
**And** updated_at字段自动更新

---

### Requirement: 菜单管理API - 删除菜单项

**描述：** 系统 MUST 允许管理员删除菜单项

**Endpoint:**
```
DELETE /api/admin/menu-items/<id>
```

**Validation Rules:**
- 菜单项必须存在
- 删除父菜单时自动删除所有子菜单（级联删除）

**Implementation Location:**
- 文件：`app.py`
- 路由：`/api/admin/menu-items/<id>`

**Validation:**
- 删除成功返回200状态
- 不存在的ID返回404
- 子菜单自动删除

#### Scenario: 删除菜单项
**Given** 管理员发送DELETE请求
**When** 删除有子菜单的菜单项
**Then** 返回200状态
**And** 父菜单和所有子菜单都被删除
**And** 数据库记录完全清除

---

### Requirement: 菜单重排序API

**描述：** 系统 MUST 允许批量更新菜单顺序

**Endpoint:**
```
POST /api/admin/menu-items/reorder
```

**Request Body:**
```json
{
  "items": [
    {"id": 1, "order": 0},
    {"id": 2, "order": 1},
    {"id": 3, "order": 2}
  ]
}
```

**Implementation Location:**
- 文件：`app.py`
- 路由：`/api/admin/menu-items/reorder`

**Validation:**
- 批量更新所有项的order字段
- 保证排序连续性（0, 1, 2...）

#### Scenario: 批量重排序
**Given** 管理员发送拖拽后的顺序
**When** POST到/reorder端点
**Then** 所有菜单项order字段更新
**And** 排序连续（0, 1, 2...）
**And** 前端显示新顺序

---

### Requirement: 前端菜单渲染API

**描述：** 系统 MUST 为前端模板提供菜单数据

**Endpoint:**
```
GET /api/menu-items
```

**Response:** 同获取列表API，但只返回visible=true的菜单项

**Implementation Location:**
- 文件：`app.py`
- 路由：`/api/menu-items`

**Validation:**
- 只返回可见菜单项
- 正确排序
- 构建正确的树形结构

#### Scenario: 前端菜单渲染
**Given** 用户访问首页
**When** GET /api/menu-items请求
**Then** 返回可见菜单项
**And** 按order排序
**And** 树形结构包含children

---

### Requirement: 菜单管理界面创建

**描述：** 系统 MUST 创建菜单管理后台页面

**URL:** `/admin/menu-management`

**Features:**
- 菜单项列表展示（树形结构）
- 添加菜单按钮
- 编辑/删除操作
- 拖拽排序
- 启用/禁用切换

**Implementation Location:**
- 文件：`templates/admin/menu_management.html`
- 文件：`app.py` 路由

**Validation:**
- 页面正确加载
- 所有功能按钮可用
- 样式与后台一致

#### Scenario: 菜单管理页面
**Given** 管理员访问/admin/menu-management
**When** 页面加载完成
**Then** 显示菜单列表和管理表单
**And** 可以添加新菜单
**And** 可以编辑/删除现有菜单

---

### Requirement: 菜单项表单

**描述：** 系统 MUST 提供创建/编辑菜单项的表单

**Form Fields:**
- label（文本输入）
- url（文本输入）
- icon（文本输入，Font Awesome类名）
- parent（选择器，可选）
- visible（复选框）

**Validation:**
- 必填字段验证
- URL格式验证
- 实时保存

#### Scenario: 菜单项表单验证
**Given** 管理员填写表单
**When** 提交空label字段
**Then** 显示验证错误
**And** 保存被阻止
**And** 填写正确后保存成功

---

### Requirement: 拖拽排序功能

**描述：** 系统 MUST 支持拖拽重新排序菜单项

**Implementation:**
- 使用SortableJS库
- 支持垂直拖拽
- 保存排序到服务器

**Validation:**
- 拖拽后顺序正确更新
- 跨层级拖拽正确处理

#### Scenario: 拖拽排序操作
**Given** 在管理页面
**When** 拖拽菜单项到新位置
**Then** 视觉反馈显示拖拽
**And** 释放后顺序更新
**And** 自动保存到服务器

---

### Requirement: base.html模板修改

**描述：** 系统 SHALL 将硬编码导航替换为动态菜单

**Location:** `templates/base.html`

**Changes:**
- 导航栏区域使用Jinja2循环渲染菜单
- 支持多级菜单（dropdown）
- 保留现有样式和Bootstrap类

**Template Code:**
```html
<ul class="navbar-nav me-auto">
{% for item in menu_items %}
    <li class="nav-item {{ 'dropdown' if item.children }}">
        <!-- 菜单渲染逻辑 -->
    </li>
{% endfor %}
</ul>
```

**Validation:**
- 菜单正确渲染
- 下拉菜单正常工作
- 样式无变化
- 移动端适配正常

#### Scenario: 前端模板渲染动态菜单
**Given** base.html模板
**When** 循环渲染menu_items变量
**Then** 所有菜单项正确显示
**And** 图标和链接正确
**And** 样式保持一致

---

### Requirement: 菜单数据加载

**描述：** 系统 SHALL 在控制器中加载菜单数据

**Location:** 所有需要显示菜单的路由

**Implementation:**
```python
menu_items = get_menu_items_for_rendering()
return render_template('template.html', menu_items=menu_items)
```

**Validation:**
- 菜单数据正确传递
- 无重复查询
- 性能良好

#### Scenario: 控制器加载菜单数据
**Given** 所有需要显示菜单的路由
**When** 渲染模板
**Then** 自动加载menu_items
**And** 传递到模板上下文
**And** 不产生N+1查询

---

### Requirement: Font Awesome图标支持

**描述：** 系统 MUST 支持为菜单项设置Font Awesome图标

**Implementation:**
- 存储图标类名（如：fas fa-home）
- 在前端渲染时显示图标
- 提供常用图标推荐

**Validation:**
- 图标正确显示
- 无图标时布局正常
- 兼容Font Awesome 6

#### Scenario: 图标显示功能
**Given** 菜单项配置了图标
**When** 前端渲染菜单
**Then** 显示对应的Font Awesome图标
**And** 无图标的菜单正常显示
**And** 图标与文字对齐正确

---

### Requirement: 菜单显示/隐藏控制

**描述：** 系统 MUST 支持启用/禁用菜单项

**Implementation:**
- visible字段控制显示
- 管理界面切换开关
- 前端只渲染可见菜单项

**Validation:**
- 切换功能正常
- 隐藏菜单不影响布局
- API正确处理visible字段

#### Scenario: 菜单显示/隐藏切换
**Given** 在管理页面
**When** 关闭visible开关
**Then** 菜单标记为隐藏
**And** 前端不再显示
**And** 布局不受影响

---

### Requirement: 多级菜单支持

**描述：** 系统 MUST 支持创建子菜单（2级）

**Implementation:**
- parent_id字段关联
- 管理界面选择父菜单
- 前端渲染下拉菜单

**Validation:**
- 2级菜单正确渲染
- 父菜单显示下拉箭头
- 子菜单正确显示

**Note:** 3级以上菜单在Phase 3实现

#### Scenario: 创建子菜单
**Given** 在管理页面
**When** 创建菜单并设置parent_id
**Then** 创建子菜单关系
**And** 父菜单显示dropdown-toggle
**And** 前端正确渲染下拉列表

---

### Requirement: 数据迁移初始化脚本

**描述：** 系统 SHALL 创建数据迁移机制

**Implementation:**
- 检查menu_items表是否存在
- 不存在则创建并插入默认数据
- 在应用启动时执行

**Location:** `app.py` `init_menu_items()`

**Validation:**
- 首次部署正常工作
- 升级部署不重复创建
- 默认数据正确

#### Scenario: 首次启动创建默认菜单
**Given** 全新部署的系统
**When** 启动应用
**Then** 自动创建menu_items表
**And** 插入4个默认菜单项（首页、文章、视频、图片）

---

## MODIFIED Requirements

### Requirement: app.py应用启动修改

**描述：** 系统 SHALL 添加菜单初始化调用

**Change Location:** `app.py` around line 100

**Added Code:**
```python
with app.app_context():
    init_homepage_config()
    init_menu_items()  # 新增
```

**Validation:**
- 启动时自动创建默认菜单
- 不影响现有功能

#### Scenario: 应用启动时初始化菜单
**Given** 应用部署在服务器上
**When** 执行python app.py启动应用
**Then** 自动调用init_menu_items()函数
**And** 创建默认4个菜单项
**And** 不影响homepage_config初始化

---

### Requirement: admin后台导航修改

**描述：** 系统 SHALL 在管理后台侧边栏添加菜单管理入口

**Change Location:** `templates/admin/base.html`

**Added Item:**
```html
<li class="nav-item">
    <a href="{{ url_for('admin_menu_management') }}" class="nav-link">
        <i class="fas fa-bars me-2"></i>菜单管理
    </a>
</li>
```

**Validation:**
- 菜单项正确显示
- 链接跳转正确
- 图标显示正常

#### Scenario: 后台导航显示菜单管理入口
**Given** 管理员登录后台
**When** 查看侧边栏导航
**Then** 显示"菜单管理"菜单项
**And** 包含fas fa-bars图标
**And** 点击可跳转到管理页面

---

## REMOVED Requirements

- **硬编码导航菜单**：从 `templates/base.html` 移除硬编码导航菜单项
  - **原代码**：`templates/base.html:121-159` 的硬编码 `<ul class="navbar-nav">`
  - **替换为**：动态菜单渲染逻辑，支持从数据库加载菜单项
  - **影响**：不再在HTML中硬编码菜单结构

---

## SCENARIOS

### 场景1：管理员添加新菜单项

**Given** 管理员登录管理后台
**When** 点击"菜单管理" -> 点击"添加菜单"
**And** 填写菜单名称"关于页面"、URL"/about"
**And** 点击"保存"
**Then** 菜单项创建成功
**And** 前端导航显示"关于页面"

---

### 场景2：管理员重新排序菜单

**Given** 在菜单管理页面
**When** 拖拽"文章"菜单到"视频"之后
**And** 释放鼠标
**And** 点击"保存"
**Then** 菜单顺序更新
**And** 前端导航按新顺序显示

---

### 场景3：管理员隐藏菜单项

**Given** 在菜单管理页面
**When** 关闭"图片"菜单的显示开关
**And** 点击"保存"
**Then** 菜单项标记为隐藏
**And** 前端导航不再显示"图片"

---

### 场景4：管理员创建子菜单

**Given** 在菜单管理页面
**When** 创建菜单项"产品"
**And** 选择父菜单为"文章"
**And** 保存
**Then** 创建子菜单
**And** 前端"文章"菜单显示下拉箭头
**And** 子菜单在下拉列表中显示

---

### 场景5：管理员删除有子菜单的父菜单

**Given** 在菜单管理页面
**When** 删除"文章"菜单（包含子菜单）
**And** 确认删除
**Then** "文章"菜单及所有子菜单被删除
**And** 前端导航不再显示

---

### 场景6：首次部署系统

**Given** 全新部署的系统
**When** 启动应用
**Then** 自动创建menu_items表
**And** 插入4个默认菜单项（首页、文章、视频、图片）
**And** 前端导航正常显示默认菜单

---

### 场景7：用户访问前端页面

**Given** 用户访问首页
**When** 页面加载
**Then** 动态菜单正确渲染
**And** 所有菜单项可点击
**And** 下拉菜单功能正常

---

## ERROR HANDLING

### 错误场景1：无效URL

**Given** 创建菜单项
**When** 输入无效URL"not-a-url"
**Then** 显示错误"请输入有效的URL"
**And** 保存失败

---

### 错误场景2：删除不存在的菜单项

**Given** 发送删除请求
**When** 菜单ID不存在
**Then** 返回404错误
**And** 显示"菜单项不存在"

---

### 错误场景3：循环引用

**Given** 更新菜单项
**When** 设置parent_id为该菜单项的子菜单ID
**Then** 拒绝更新
**And** 显示错误"不能创建循环引用"

---

## PERFORMANCE REQUIREMENTS

### 要求1：数据库查询优化

- 菜单查询添加适当索引
- 前端菜单加载使用预加载（joinedload）
- 避免N+1查询问题

### 要求2：缓存策略

- 菜单数据可缓存（可选）
- 缓存时间：5分钟
- 变更菜单时清除缓存

### 要求3：响应时间

- 菜单管理页面加载 < 500ms
- 保存操作响应 < 1s
- 拖拽排序响应 < 300ms

---

## SECURITY REQUIREMENTS

### 1. 权限控制

- 所有管理API需要管理员权限（@login_required）
- 前端菜单API允许匿名访问（只读）

### 2. 输入验证

- label长度限制：1-50字符
- URL长度限制：1-200字符
- icon长度限制：1-50字符
- 特殊字符转义

### 3. XSS防护

- 对所有用户输入进行HTML转义
- menu_items.html使用|escape过滤器

---

## BACKWARD COMPATIBILITY

- 不修改现有数据表结构
- 不影响现有路由和API
- 保持前端URL不变
- 现有页面导航不受影响

---

**版本：** 1.0
**最后更新：** 2025-10-29
**状态：** 待审核
