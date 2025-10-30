# Tasks: 实现CMS中英双语切换功能

## Implementation Tasks

- [x] **任务1: 配置Flask-Babel国际化框架**
  - 在app.py中配置Babel
  - 设置语言选择器函数
  - 添加翻译上下文处理器
  - 文件: app.py

- [x] **任务2: 标记模板中的静态文本**
  - 标记base.html中的文本
  - 标记index.html中的文本
  - 标记admin/base.html中的文本
  - 文件: templates/base.html, templates/index.html, templates/admin/base.html

- [x] **任务3: 生成和配置翻译文件**
  - 创建babel.cfg配置文件
  - 使用pybabel提取翻译文本
  - 更新中文和英文翻译文件
  - 编译翻译文件为.mo格式
  - 文件: babel.cfg, translations/*.po, translations/*.mo

- [x] **任务4: 添加英文翻译**
  - 为所有标记的文本提供英文翻译
  - 包括前台和后台所有界面文本
  - 文件: translations/en_US/LC_MESSAGES/messages.po

- [x] **任务5: 实现菜单项多语言支持**
  - 创建MENU_TRANSLATIONS映射字典
  - 修改inject_globals()函数应用翻译
  - 支持主菜单和子菜单翻译
  - 文件: app.py

- [x] **任务6: 实现首页配置多语言支持**
  - 创建HOMEPAGE_CONFIG_TRANSLATIONS映射字典
  - 修改index()函数翻译配置内容
  - 翻译Hero区域和内容区域标题
  - 文件: app.py

- [x] **任务7: 修复模板语法错误**
  - 移除{% trans %}标签中的变量引用
  - 确保模板语法正确
  - 文件: templates/base.html, templates/index.html

- [x] **任务8: 添加语言切换路由**
  - 实现/set_language/<lang>路由
  - 支持session存储语言偏好
  - 自动重定向到上一页
  - 文件: app.py

- [x] **任务9: 添加导航栏语言切换器**
  - 在base.html中添加下拉菜单
  - 显示当前语言
  - 提供语言切换链接
  - 文件: templates/base.html

- [x] **任务10: 测试和验证**
  - 测试英文页面显示
  - 测试中文页面显示
  - 测试语言切换功能
  - 测试Session持久化
  - 验证所有文本正确翻译

- [x] **任务11: 创建文档**
  - 创建LANG_SWITCH_FIX.md说明文档
  - 创建FINAL_LANG_FIX.md完整文档
  - 记录技术实现和使用方法
  - 文件: LANG_SWITCH_FIX.md, FINAL_LANG_FIX.md

## Validation Tasks

- [x] **验证1: 前台页面双语支持**
  - 访问/确认页面标题正确翻译
  - 确认导航菜单正确翻译
  - 确认Hero区域正确翻译
  - 确认按钮文本正确翻译

- [x] **验证2: 后台管理双语支持**
  - 确认登录页面正确翻译
  - 确认侧边栏菜单正确翻译
  - 确认页面标题正确翻译

- [x] **验证3: 动态内容翻译**
  - 确认数据库菜单项正确翻译
  - 确认首页配置正确翻译

- [x] **验证4: 语言切换功能**
  - 确认URL切换工作正常
  - 确认导航栏切换工作正常
  - 确认Session持久化正常

## Order of Execution

Tasks should be executed in the order listed above, as some tasks depend on others:
1. 配置Flask-Babel是所有其他任务的基础
2. 模板标记需要在翻译文件生成之前完成
3. 静态文本翻译完成后才能处理动态数据翻译
4. 所有实现完成后才能进行测试验证
