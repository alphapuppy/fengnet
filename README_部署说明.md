# 游戏部署说明

## 方法一：使用 Python（推荐，最简单）

### 步骤：
1. 确保已安装 Python（Python 3.x）
   - 如果没有，从 https://www.python.org/downloads/ 下载安装

2. 双击运行 `start_server.bat` 文件
   - 或者在命令行中运行：`python start_server.py`

3. 服务器启动后，会显示访问地址：
   - **本地访问**：`http://localhost:8000/DOCTYPE.html`
   - **局域网访问**：`http://你的IP地址:8000/DOCTYPE.html`

4. 在同一局域网的其他设备（手机、平板等）可以通过局域网IP访问

---

## 方法二：使用 Node.js

### 步骤：
1. 安装 Node.js（如果没有）：https://nodejs.org/

2. 安装 http-server：
   ```bash
   npm install -g http-server
   ```

3. 在项目目录运行：
   ```bash
   http-server -p 8000
   ```

4. 访问：`http://localhost:8000/DOCTYPE.html`

---

## 方法三：使用 VS Code Live Server

1. 在 VS Code 中安装 "Live Server" 扩展
2. 右键点击 `DOCTYPE.html` 文件
3. 选择 "Open with Live Server"
4. 会自动打开浏览器并显示本地地址

---

## 方法四：部署到云服务器

### 如果要在公网访问，可以部署到：
- **GitHub Pages**（免费）
- **Vercel**（免费）
- **Netlify**（免费）
- **自己的云服务器**（需要购买）

### GitHub Pages 部署步骤：
1. 创建 GitHub 仓库
2. 上传所有文件（DOCTYPE.html 和图片文件）
3. 在仓库设置中启用 GitHub Pages
4. 选择主分支作为源
5. 访问：`https://你的用户名.github.io/仓库名/DOCTYPE.html`

---

## 注意事项

1. **防火墙设置**：
   - 如果局域网其他设备无法访问，需要：
     - Windows：在防火墙中允许 Python/Node.js 通过防火墙
     - 或者临时关闭防火墙测试

2. **文件路径**：
   - 确保所有图片文件（feng3_PhotoGrid.png, cyp1.png, marry2.png, ping.png, marry.png）都在同一目录下

3. **端口占用**：
   - 如果 8000 端口被占用，可以修改脚本中的 `PORT = 8000` 为其他端口（如 8080, 3000 等）

---

## 快速测试

运行服务器后，在同一局域网的手机上：
1. 确保手机和电脑连接同一个 WiFi
2. 在手机浏览器输入：`http://电脑IP:8000/DOCTYPE.html`
3. 即可在手机上玩游戏！

