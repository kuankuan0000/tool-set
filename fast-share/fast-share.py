#!/usr/bin/env python3
"""
Fast Share - 一个简单的文件分享工具

使用方法:
    fast-share.py [-h] [-p PORT] [--auto-close] file

示例:
    # 分享文件（使用随机端口）
    fast-share.py myfile.txt

    # 使用指定端口分享文件
    fast-share.py -p 8000 myfile.txt

    # 分享文件并在第一次下载后自动关闭
    fast-share.py --auto-close myfile.txt

参数说明:
    file          要分享的文件路径
    -p, --port    指定服务器端口（默认使用随机端口）
    --auto-close  在第一次下载完成后自动关闭服务器
    -h, --help    显示帮助信息
"""

import http.server
import socketserver
import os
import random
import argparse
import socket
import subprocess
import re

def fast_share(file_path, port=None, auto_close=False):
    file_path = os.path.abspath(file_path)
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return

    if port is None:
        port = random.randint(10000, 65535)
    dir_path, file_name = os.path.split(file_path)

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == f"/{file_name}":
                super().do_GET()
                if auto_close:
                    print("\nFile downloaded. Server is shutting down...")
                    os._exit(0)
            else:
                self.send_error(404, "File not found")

    # 启动服务器
    os.chdir(dir_path)
    try:
        with socketserver.TCPServer(("", port), CustomHandler) as httpd:
            urls = generate_possible_urls(port, file_name)
            print(f"Sharing {file_name} at the following URLs:\n")
            for url in urls:
                print(url)
            if auto_close:
                print("\nServer will automatically exit after first download.")
            print("\nPress Ctrl+C to stop sharing.")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nShutting down the server ...")
            finally:
                httpd.server_close()
    except OSError as e:
        if e.errno == 98 or e.errno == 10048:  # Linux/Windows 端口被占用的错误码
            print(f"Error: Port {port} is already in use.")
        else:
            raise

def generate_possible_urls(port, file_name):
    """
    列出所有可能的局域网 IP 地址 URL。
    """
    possible_urls = []
    ip_addresses = get_all_ip_addresses()
    for ip in ip_addresses:
        possible_urls.append(f"http://{ip}:{port}/{file_name}")
    return possible_urls

def get_all_ip_addresses():
    """
    获取所有有效的局域网 IP 地址。
    """
    ip_addresses = []
    try:
        # macOS 和 Linux 使用 ifconfig
        if os.name != "nt":
            output = subprocess.check_output("ifconfig", shell=True, encoding="utf-8")
            ip_addresses = parse_ips_from_ifconfig(output)
        else:
            # Windows 使用 ipconfig
            output = subprocess.check_output("ipconfig", encoding="utf-8")
            ip_addresses = parse_ips_from_ipconfig(output)
    except Exception as e:
        print(f"Error fetching IP addresses: {e}")

    # 回退到 localhost
    if not ip_addresses:
        ip_addresses.append("127.0.0.1")
    return ip_addresses

def parse_ips_from_ifconfig(output):
    """
    从 macOS/Linux 的 ifconfig 输出中解析 IP 地址。
    """
    ipv4_pattern = r"inet\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"
    matches = re.findall(ipv4_pattern, output)
    return [ip for ip in matches if not ip.startswith("127.") and not ip.startswith("198.18.")]

def parse_ips_from_ipconfig(output):
    """
    从 Windows 的 ipconfig 输出中解析局域网 IP。
    """
    ipv4_pattern = r"IPv4 Address.*?:\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"
    matches = re.findall(ipv4_pattern, output)
    return [ip for ip in matches if not ip.startswith("127.") and not ip.startswith("198.18.")]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="快速分享文件的命令行工具。",
        epilog="""
示例:
  %(prog)s myfile.txt                # 使用随机端口分享文件
  %(prog)s -p 8000 myfile.txt        # 使用指定端口 8000 分享文件
  %(prog)s --auto-close myfile.txt   # 分享文件并在首次下载后自动退出
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("file", help="要分享的文件路径")
    parser.add_argument("-p", "--port", type=int, help="指定服务器端口（默认：随机端口）")
    parser.add_argument("--auto-close", action="store_true", help="在第一次下载完成后自动退出程序")
    args = parser.parse_args()

    fast_share(args.file, args.port, args.auto_close)