# Spec: CMS多语言支持功能

## ADDED Requirements

#### Requirement: 支持中英双语界面
**Description**: CMS系统必须支持中文和英文两种语言的用户界面
**Acceptance Criteria**:
- [ ] 系统启动时默认显示中文界面
- [ ] 可以切换到英文界面
- [ ] 可以切换回中文界面
- [ ] 页面HTML lang属性正确设置为当前语言

**Scenario 1: 默认语言**
- Given 用户访问首页
- Then 页面显示中文内容
- And HTML lang="zh_CN"

**Scenario 2: 切换到英文**
- Given 用户在中文页面
- When 用户访问 /set_language/en
- Then 页面重定向到上一页
- And 页面显示英文内容
- And HTML lang="en"

**Scenario 3: 切换到中文**
- Given 用户在英文页面
- When 用户访问 /set_language/zh_CN
- Then 页面重定向到上一页
- And 页面显示中文内容
- And HTML lang="zh_CN"

---

#### Requirement: 前台页面完整翻译
**Description**: 所有前台展示页面必须支持完整的中英双语翻译
**Acceptance Criteria**:
- [ ] 页面标题正确翻译
- [ ] 导航菜单正确翻译
- [ ] Hero区域内容正确翻译
- [ ] 按钮文本正确翻译
- [ ] 内容区域标题正确翻译
- [ ] 提示信息正确翻译
- [ ] 页脚信息正确翻译

**Scenario 1: 首页英文显示**
- Given 用户访问英文首页
- Then 显示"Welcome to AI-CMS"
- And 显示"Home, Articles, Videos, Images"导航菜单
- And 显示"Read Articles, Watch Videos"按钮
- And 显示"Latest Articles, Latest Videos, Latest Images"区域标题
- And 显示"View More"按钮

**Scenario 2: 首页中文显示**
- Given 用户访问中文首页
- Then 显示"欢迎来到AI-CMS"
- And 显示"首页, 文章, 视频, 图片"导航菜单
- And 显示"阅读文章, 观看视频"按钮
- And 显示"最新文章, 最新视频, 最新图片"区域标题
- And 显示"查看更多"按钮

**Scenario 3: 菜单项翻译**
- Given 当前语言为英文
- Then 菜单显示"Home"而不是"首页"
- And 菜单显示"Articles"而不是"文章"
- And 菜单显示"Videos"而不是"视频"
- And 菜单显示"Images"而不是"图片"

**Scenario 4: 按钮翻译**
- Given 当前语言为英文
- Then "阅读文章"按钮显示为"Read Articles"
- And "观看视频"按钮显示为"Watch Videos"
- And "查看更多"按钮显示为"View More"
- And "查看大图"按钮显示为"View Full Size"

**Scenario 5: 提示信息翻译**
- Given 当前语言为英文且无内容时
- Then 显示"No Articles Yet"而不是"暂无文章"
- And 显示"No Videos Yet"而不是"暂无视频"
- And 显示"No Images Yet"而不是"暂无图片"

---

#### Requirement: 后台管理界面完整翻译
**Description**: 所有后台管理页面必须支持完整的中英双语翻译
**Acceptance Criteria**:
- [ ] 登录页面正确翻译
- [ ] 侧边栏菜单正确翻译
- [ ] 页面标题正确翻译
- [ ] 表单标签正确翻译
- [ ] 按钮文本正确翻译

**Scenario 1: 后台登录页英文**
- Given 用户访问英文后台登录页
- Then 显示"CMS Admin Panel"而不是"CMS管理后台"
- And 显示"Admin Login"而不是"管理员登录"
- And 显示"Username"而不是"用户名"
- And 显示"Password"而不是"密码"
- And 显示"Login"而不是"登录"

**Scenario 2: 后台菜单英文**
- Given 用户在英文后台
- Then 侧边栏显示"Dashboard"而不是"仪表盘"
- And 显示"Article Management"而不是"文章管理"
- And 显示"Video Management"而不是"视频管理"
- And 显示"Image Management"而不是"图片管理"
- And 显示"Layout Management"而不是"版面管理"

---

#### Requirement: 多种语言切换方式
**Description**: 用户必须能够通过多种方式切换语言
**Acceptance Criteria**:
- [ ] 通过URL参数切换语言
- [ ] 通过导航栏下拉菜单切换语言
- [ ] 通过浏览器Accept-Language自动选择
- [ ] 语言设置跨页面保持

**Scenario 1: URL切换**
- Given 用户访问 /set_language/en
- When 用户跳转到首页
- Then 页面显示英文

**Scenario 2: 导航栏切换**
- Given 用户在中文页面
- When 用户点击右上角语言切换按钮
- And 用户选择"English"
- Then 页面切换到英文

**Scenario 3: 浏览器自动检测**
- Given 用户浏览器Accept-Language为en-US
- When 用户首次访问首页
- Then 页面显示英文

**Scenario 4: Session持久化**
- Given 用户切换到英文
- When 用户访问任意其他页面
- Then 页面保持英文显示

---

#### Requirement: 动态内容翻译
**Description**: 数据库中存储的动态内容（如菜单、配置）必须支持翻译
**Acceptance Criteria**:
- [ ] 菜单标签根据当前语言显示
- [ ] 首页配置标题根据当前语言显示
- [ ] 按钮文本根据当前语言显示
- [ ] 区域标题根据当前语言显示

**Scenario 1: 菜单翻译**
- Given 数据库存储菜单标签"首页"
- When 当前语言为英文
- Then 导航栏显示"Home"
- When 当前语言为中文
- Then 导航栏显示"首页"

**Scenario 2: Hero区域翻译**
- Given 数据库存储hero标题"欢迎来到AI-CMS"
- When 当前语言为英文
- Then 显示"Welcome to AI-CMS"
- When 当前语言为中文
- Then 显示"欢迎来到AI-CMS"

**Scenario 3: 配置按钮翻译**
- Given 数据库存储button1_text"阅读文章"
- When 当前语言为英文
- Then 按钮显示"Read Articles"
- When 当前语言为中文
- Then 按钮显示"阅读文章"

---

#### Requirement: 翻译文件管理
**Description**: 必须提供完整的翻译文件管理系统
**Acceptance Criteria**:
- [ ] 生成.po翻译模板文件
- [ ] 提供完整的英文翻译
- [ ] 编译生成.mo二进制文件
- [ ] 支持动态添加新翻译

**Scenario 1: 提取翻译**
- Given 开发者在模板中添加{% trans %}标记
- When 运行 pybabel extract
- Then 生成messages.pot模板文件
- And 包含所有标记的文本

**Scenario 2: 更新翻译文件**
- Given 存在messages.pot模板
- When 运行 pybabel update
- Then 更新zh_CN和en_US的.po文件
- And 保留已有翻译

**Scenario 3: 编译翻译**
- Given 存在.po翻译文件
- When 运行 pybabel compile
- Then 生成.mo二进制文件
- And 应用可以读取翻译

---

#### Requirement: 翻译验证和测试
**Description**: 必须提供完整的功能验证和测试方法
**Acceptance Criteria**:
- [ ] 提供自动化测试脚本
- [ ] 提供手动测试指南
- [ ] 验证所有页面翻译正确性
- [ ] 验证语言切换功能正常

**Scenario 1: 英文页面验证**
- Given 用户访问英文页面
- When 检查页面内容
- Then 所有文本为英文
- And HTML lang="en"

**Scenario 2: 中文页面验证**
- Given 用户访问中文页面
- When 检查页面内容
- Then 所有文本为中文
- And HTML lang="zh_CN"

**Scenario 3: 语言切换验证**
- Given 用户在中文页面
- When 用户切换到英文
- Then 页面立即更新为英文
- And 刷新后保持英文设置

---

## MODIFIED Requirements

#### Modified: 现有模板必须支持国际化标记
**Description**: 现有模板文件需要添加{% trans %}标记以支持翻译
**Changes**:
- templates/base.html: 添加页面标题、菜单、页脚的{% trans %}标记
- templates/index.html: 添加首页所有文本的{% trans %}标记
- templates/admin/base.html: 添加后台管理界面文本的{% trans %}标记

**Impact**:
- 需要修改现有模板文件
- 不影响现有功能
- 向后兼容

---

#### Modified: 应用初始化流程
**Description**: 应用启动时需要初始化Babel和翻译相关配置
**Changes**:
- 在app.py中配置Babel
- 添加语言检测函数
- 添加上下文处理器
- 添加翻译映射字典

**Impact**:
- 增加应用启动时间（<100ms）
- 增加内存占用（翻译文件缓存）
- 不影响现有API和路由

---

## REMOVED Requirements

无

---

## Dependencies

- Flask-Babel 2.x或更高版本
- Python gettext模块
- 现有的CMS数据库结构（无需修改）
- 现有的路由和视图函数（无需修改）

---

## Acceptance Testing

### Manual Testing Checklist
- [ ] 访问英文页面验证所有文本显示英文
- [ ] 访问中文页面验证所有文本显示中文
- [ ] 使用URL切换语言验证重定向正确
- [ ] 使用导航栏切换语言验证UI更新
- [ ] 刷新页面验证语言设置保持
- [ ] 打开新标签页验证语言设置保持
- [ ] 验证后台管理界面翻译正确
- [ ] 验证动态内容（菜单、配置）翻译正确

### Automated Testing (Future)
- [ ] 单元测试：验证翻译函数
- [ ] 单元测试：验证语言检测逻辑
- [ ] 集成测试：验证页面渲染语言正确性
- [ ] 端到端测试：验证用户切换语言流程

---

## Rollout Plan

1. **阶段1**: 配置Flask-Babel框架
2. **阶段2**: 标记模板静态文本
3. **阶段3**: 生成和配置翻译文件
4. **阶段4**: 添加英文翻译
5. **阶段5**: 实现动态内容翻译映射
6. **阶段6**: 添加语言切换UI
7. **阶段7**: 测试和验证
8. **阶段8**: 部署和监控

---

## Metrics

- **功能覆盖率**: 100%（所有界面元素）
- **翻译完整度**: 100%（所有标记文本）
- **性能影响**: < 100ms应用启动时间
- **内存占用**: 翻译文件缓存 < 5MB
- **用户满意度**: 可通过A/B测试验证
