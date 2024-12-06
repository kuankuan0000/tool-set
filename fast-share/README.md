# Fast Share

Fast Share 是一个轻量级的命令行文件分享工具，可以快速创建一个临时的 HTTP 服务器来分享单个文件。它会自动检测你的本地 IP 地址，并生成可访问的 URL，方便局域网内的其他设备下载文件。

## 特性

- 快速分享单个文件
- 自动检测并显示所有可用的局域网 IP 地址
- 支持自定义端口
- 支持下载完成后自动关闭服务器
- 跨平台支持（Windows/macOS/Linux）

## 安装

1. 确保你的系统已安装 Python 3.x

2. 下载 `fast-share.py` 文件

3. 使其在系统层面可用：

   **Linux/macOS:**
   ```bash
   # 1. 移动脚本到 bin 目录
   sudo cp fast-share.py /usr/local/bin/fast-share

   # 2. 添加执行权限
   sudo chmod +x /usr/local/bin/fast-share
   ```

   **Windows:**   
   ```powershell
   # 1. 创建一个适当的目录（如果还没有的话）
   mkdir C:\Users\<用户名>\AppData\Local\Programs\Scripts

   # 2. 复制脚本到该目录
   copy fast-share.py C:\Users\<用户名>\AppData\Local\Programs\Scripts\fast-share.py

   # 3. 将该目录添加到系统环境变量 PATH 中
   # 可以通过系统设置 > 系统 > 关于 > 高级系统设置 > 环境变量 来添加
   ```

## 使用方法

基本用法：
```bash
fast-share <文件路径>
```

### 命令行选项

```bash
fast-share [-h] [-p PORT] [--auto-close] file
```

- `file`: 要分享的文件路径
- `-p, --port`: 指定服务器端口（默认使用随机端口）
- `--auto-close`: 在第一次下载完成后自动退出程序
- `-h, --help`: 显示帮助信息

### 使用示例

1. 分享文件（使用随机端口）：
   ```bash
   fast-share myfile.txt
   ```

2. 使用指定端口分享文件：
   ```bash
   fast-share -p 8000 myfile.txt
   ```

3. 分享文件并在首次下载后自动关闭：
   ```bash
   fast-share --auto-close myfile.txt
   ```

## 注意事项

1. 确保防火墙允许所选端口的访问
2. 默认情况下，服务器会一直运行直到你按 Ctrl+C 停止它
3. 使用 `--auto-close` 选项时，服务器会在文件被下载一次后自动关闭
4. 该工具仅建议在可信任的局域网环境中使用

## 贡献

欢迎提交 Issues 和 Pull Requests 来改进这个工具。

## 许可

GPL-3.0 License