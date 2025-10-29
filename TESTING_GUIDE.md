# 🧪 封面图片选择功能测试指南

## 📋 问题症状
- 从图片库选择封面图片后界面卡住不动

## 🔍 调试方法

### 步骤1：打开开发者工具
1. 在浏览器中打开编辑页面：`http://localhost:8080/admin/articles/2/edit`
2. 按 `F12` 键（或右键 → 检查）
3. 切换到 **Console**（控制台）选项卡
4. 清空控制台（点击清除按钮或按 `Ctrl+L`）

### 步骤2：测试功能
1. 点击 **"从图片库选择"** 按钮
2. 观察控制台输出，应该看到：
   ```
   ✅ showCoverImagePicker 被调用
   ✅ showImagePickerModal 被调用，图片数量: X
   ```
3. 点击任意图片卡片
4. 观察控制台输出，应该看到：
   ```
   ✅ 选择了图片: /static/uploads/images/xxx.jpg
   ✅ 准备调用 setCoverImage
   ✅ setCoverImage 被调用: /static/uploads/images/xxx.jpg
   ✅ 获取到 input 元素: <input id="coverImageInput" ...>
   ✅ 已保存到数据库 (去掉 /static/): uploads/images/xxx.jpg
   ✅ 显示用URL: /static/uploads/images/xxx.jpg
   ✅ 获取到 selectorDiv: <div class="cover-image-selector">...
   ✅ 获取到 currentCoverDiv: null (或现有元素)
   ✅ 创建新的封面预览 (或更新现有封面预览)
   ✅ setCoverImage 执行完成
   ✅ setCoverImage 调用完成
   ✅ 准备关闭模态框
   ✅ 模态框已关闭
   ```

### 步骤3：分析问题

#### ✅ 正常情况
- 所有步骤都有 ✅ 标记的日志输出
- 模态框关闭
- 封面预览显示

#### ❌ 异常情况

**情况1：点击图片后没反应**
- 检查是否有JavaScript错误（红色错误信息）
- 可能是模态框事件绑定失败

**情况2：setCoverImage 调用失败**
- 错误信息会显示具体的错误原因
- 常见问题：元素找不到

**情况3：模态框没有关闭**
- 检查最后的日志是否到达"✅ 模态框已关闭"
- 如果没有，可能是modal.remove()出错

## 🔧 强制刷新

如果看到旧代码，清除浏览器缓存：

### Chrome/Edge
1. 按 `Ctrl+Shift+Delete`
2. 选择"缓存的图片和文件"
3. 点击"清除数据"
4. 刷新页面

### 或者硬刷新
- 按 `Ctrl+F5` (Windows/Linux)
- 按 `Cmd+Shift+R` (Mac)

## 📊 快速验证

运行测试脚本：
```bash
curl http://localhost:8080/test-js
```

访问测试页面并点击按钮，检查控制台输出。

## 🎯 预期结果

如果一切正常：
- [ ] 模态框正常弹出
- [ ] 图片列表正常显示
- [ ] 点击图片后模态框关闭
- [ ] 封面预览正确显示
- [ ] 无JavaScript错误

## 📝 报告问题

如果仍有问题，请提供：
1. 浏览器控制台的完整日志
2. 具体的错误信息（如果有）
3. 哪一步没有按预期执行

---

*更新时间: 2025-10-28 10:11*