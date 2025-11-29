# 修复 Git 权限问题

## 问题原因
当前远程仓库指向 `alphapuppy/fengnet.git`，但你的账户 `is-johnee` 没有该仓库的写入权限。

## 解决方案

### 方案一：创建你自己的仓库（推荐）

1. **在 GitHub 上创建新仓库**
   - 登录 GitHub（使用 `is-johnee` 账户）
   - 点击右上角 `+` → `New repository`
   - 仓库名：`fengnet` 或 `cyber-love-520`
   - 选择 `Public`
   - 点击 `Create repository`

2. **修改远程仓库地址**

   在项目目录执行：
   ```bash
   # 删除旧的远程仓库
   git remote remove origin
   
   # 添加你的新仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   
   # 推送代码
   git push -u origin main
   ```

### 方案二：使用 Personal Access Token（如果必须推送到 alphapuppy 的仓库）

1. **生成 Personal Access Token**
   - GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - 点击 `Generate new token (classic)`
   - 勾选 `repo` 权限
   - 生成并复制 token

2. **使用 Token 推送**
   ```bash
   # 推送时使用 token 作为密码
   git push -u origin main
   # 用户名：alphapuppy
   # 密码：粘贴你的 token
   ```

### 方案三：使用 SSH（推荐长期使用）

1. **生成 SSH 密钥**（如果还没有）
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. **添加 SSH 密钥到 GitHub**
   - 复制 `~/.ssh/id_ed25519.pub` 的内容
   - GitHub → Settings → SSH and GPG keys → New SSH key
   - 粘贴并保存

3. **修改远程地址为 SSH**
   ```bash
   git remote set-url origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

