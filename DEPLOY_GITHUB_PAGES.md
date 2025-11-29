# GitHub Pages 部署详细步骤

## 📋 前置准备

1. 确保已安装 Git
   - 下载地址：https://git-scm.com/downloads

2. 拥有 GitHub 账号
   - 如果没有，去 https://github.com 注册

---

## 🚀 部署步骤

### 第一步：创建 GitHub 仓库

1. 登录 GitHub
2. 点击右上角 `+` → `New repository`
3. 填写仓库信息：
   - **Repository name**: `cyber-love-520`（或你喜欢的名字）
   - **Description**: 浪漫的赛博跑酷游戏
   - **Visibility**: 选择 `Public`（GitHub Pages 免费版需要公开仓库）
   - **不要**勾选 "Initialize this repository with a README"
4. 点击 `Create repository`

### 第二步：初始化本地 Git 仓库

在项目文件夹中打开命令行（或 Git Bash），执行：

```bash
# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交文件
git commit -m "Initial commit: 游戏初始版本"

# 添加远程仓库（替换 YOUR_USERNAME 和 YOUR_REPO_NAME）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

**注意**：将 `YOUR_USERNAME` 替换为你的 GitHub 用户名，`YOUR_REPO_NAME` 替换为你的仓库名。

### 第三步：启用 GitHub Pages

#### 方法一：使用 GitHub Actions（推荐，已自动配置）

1. 仓库已经包含了 `.github/workflows/deploy.yml` 文件
2. 推送代码后，GitHub Actions 会自动部署
3. 在仓库页面，点击 `Settings` → `Pages`
4. 在 "Source" 中选择 `GitHub Actions`
5. 等待部署完成（通常 1-2 分钟）

#### 方法二：使用传统方式

1. 在仓库页面，点击 `Settings`（设置）
2. 左侧菜单找到 `Pages`
3. 在 "Source" 中选择：
   - Branch: `main`（或 `master`）
   - Folder: `/ (root)`
4. 点击 `Save`
5. 等待几分钟，GitHub 会生成你的网站地址

### 第四步：访问你的游戏

部署完成后，访问地址为：

```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/feng.html
```

例如：
```
https://zhangsan.github.io/cyber-love-520/feng.html
```

---

## 🔄 更新游戏

每次修改代码后，推送更新：

```bash
git add .
git commit -m "更新游戏内容"
git push
```

GitHub Pages 会自动重新部署（通常需要 1-2 分钟）。

---

## ⚙️ 高级配置

### 使用自定义域名

1. 在仓库 `Settings` → `Pages` → `Custom domain`
2. 输入你的域名（如 `game.example.com`）
3. 在你的域名 DNS 设置中添加 CNAME 记录

### 使用 index.html 作为首页

如果你想直接访问 `https://你的用户名.github.io/仓库名/` 就能玩游戏：

1. 将 `feng.html` 重命名为 `index.html`
2. 或者保持现状，访问时加上 `/feng.html`

---

## ❓ 常见问题

### Q: 为什么我的网站显示 404？

A: 
- 检查仓库是否为 Public（公开）
- 等待几分钟让 GitHub 完成部署
- 确认访问的 URL 路径正确

### Q: 图片加载不出来？

A:
- 确保所有图片文件都已上传到仓库
- 检查图片文件名是否与代码中的一致
- 清除浏览器缓存

### Q: 如何查看部署状态？

A:
- 在仓库页面点击 `Actions` 标签
- 可以看到部署进度和日志

### Q: 可以设置为私有仓库吗？

A:
- GitHub Pages 免费版只支持公开仓库
- 如果需要私有仓库，需要 GitHub Pro 账号

---

## 📱 分享给朋友

部署完成后，你可以：

1. 直接分享链接给朋友
2. 在任何设备上访问（手机、平板、电脑）
3. 无需安装任何软件，打开浏览器就能玩！

---

## 🎉 完成！

现在你的游戏已经部署到 GitHub Pages 了！

访问地址：`https://你的用户名.github.io/仓库名/feng.html`

享受你的游戏吧！🎮✨

