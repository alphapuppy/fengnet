@echo off
echo 正在清除 GitHub 的 Git 凭据...
echo.

REM 清除 Windows 凭据管理器中的 GitHub 凭据
cmdkey /delete:git:https://github.com 2>nul
cmdkey /delete:git:https://github.com/alphapuppy 2>nul

echo.
echo 凭据已清除！
echo.
echo 现在请执行：git push -u origin main
echo 系统会提示你输入用户名和密码
echo 用户名：alphapuppy
echo 密码：使用 Personal Access Token（不是账户密码）
echo.
echo 如何获取 Token：
echo 1. 打开 https://github.com/settings/tokens
echo 2. 点击 "Generate new token (classic)"
echo 3. 勾选 "repo" 权限
echo 4. 生成并复制 token
echo.
pause

