# Fast Share

Fast Share 是一个轻量级的命令行文件分享工具，专为局域网内快速分享文件设计。它会自动创建一个临时的 HTTP 服务器，智能识别最优的局域网 IP 地址，并生成便捷的 curl 下载命令，特别适合在开发环境中的文件传输场景。

默认采用"即用即走"模式：文件下载完成后自动关闭服务器，也可以选择保持服务器运行以支持多次下载。

## 特性

- 快速分享单个文件
- 智能识别最优局域网 IP 地址
- 支持自定义端口
- 默认单次下载模式（下载完成后自动关闭）
- 支持保持服务器持续运行
- 自动处理文本文件的 UTF-8 编码
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
fast-share [-h] [-p PORT] [--keep-alive] file
```

- `file`: 要分享的文件路径
- `-p, --port`: 指定服务器端口（默认使用随机端口）
- `--keep-alive`: 保持服务器运行，不会在文件下载后自动退出
- `-h, --help`: 显示帮助信息

### 使用示例

1. 分享文件（使用随机端口，下载后自动关闭）：
   ```bash
   fast-share myfile.txt
   ```

2. 使用指定端口分享文件：
   ```bash
   fast-share -p 8000 myfile.txt
   ```

3. 分享文件并保持服务器运行：
   ```bash
   fast-share --keep-alive myfile.txt
   ```

## 特殊功能

### 智能 IP 地址选择
工具会自动识别最可能需要的局域网 IP 地址，并将其作为主要地址显示。其他可用地址会作为备选地址列出。

### 文本文件编码支持
对于常见的文本文件（.txt、.md、.py、.json、.xml、.html 等），工具会自动设置正确的 UTF-8 编码，确保文件内容能够正确显示。

### 便捷的 curl 命令
工具会自动生成对应的 curl 下载命令，方便在命令行中快速复制使用：
```bash
$ fast-share README.md
Sharing README.md at the following URLs:
URL:  http://10.0.210.85:43011/README.md
curl: curl -O http://10.0.210.85:43011/README.md
```

## 注意事项

1. 确保防火墙允许所选端口的访问
2. 默认情况下，服务器会在文件被下载一次后自动关闭
3. 使用 `--keep-alive` 选项可以保持服务器持续运行
4. 该工具仅建议在可信任的局域网环境中使用

## 贡献

欢迎提交 Issues 和 Pull Requests 来改进这个工具。

## 许可

GPL-3.0 License