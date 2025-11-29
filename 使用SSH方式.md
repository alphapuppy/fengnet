# 使用 SSH 方式推送（推荐，更安全）

## 步骤

### 1. 检查是否已有 SSH 密钥

```bash
ls ~/.ssh/id_ed25519.pub
```

如果没有，生成新的 SSH 密钥：

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

按 Enter 使用默认路径，可以设置密码或留空。

### 2. 复制公钥内容

```bash
cat ~/.ssh/id_ed25519.pub
```

或者 Windows 上：
```bash
type %USERPROFILE%\.ssh\id_ed25519.pub
```

### 3. 添加到 GitHub

1. 打开 https://github.com/settings/keys
2. 点击 "New SSH key"
3. Title: 随便填（如 "My PC"）
4. Key: 粘贴刚才复制的公钥内容
5. 点击 "Add SSH key"

### 4. 修改远程仓库地址为 SSH

```bash
git remote set-url origin git@github.com:alphapuppy/fengnet.git
```

### 5. 测试连接

```bash
ssh -T git@github.com
```

应该看到：`Hi alphapuppy! You've successfully authenticated...`

### 6. 推送代码

```bash
git push -u origin main
```

现在不需要输入密码了！

