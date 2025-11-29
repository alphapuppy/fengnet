#!/usr/bin/env python3
"""
简单的HTTP服务器，用于部署游戏
使用方法：python start_server.py
"""

import http.server
import socketserver
import os
import webbrowser
import socket

# 获取本机IP地址
def get_local_ip():
    try:
        # 连接到一个远程地址（不实际发送数据）
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# 设置端口
PORT = 8000

# 切换到脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 创建服务器
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    local_ip = get_local_ip()
    print("=" * 60)
    print("游戏服务器已启动！")
    print("=" * 60)
    print(f"本地访问: http://localhost:{PORT}/DOCTYPE.html")
    print(f"本地访问: http://127.0.0.1:{PORT}/DOCTYPE.html")
    print(f"局域网访问: http://{local_ip}:{PORT}/DOCTYPE.html")
    print("=" * 60)
    print("按 Ctrl+C 停止服务器")
    print("=" * 60)
    
    # 自动打开浏览器
    try:
        webbrowser.open(f"http://localhost:{PORT}/DOCTYPE.html")
    except:
        pass
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")

