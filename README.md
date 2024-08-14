# 🖥️ PyMyHttpServer - Simple HTTP Server 🖥️

![PyMyHttpServer](asset/main.png)

This Python script sets up a basic HTTP server that serves static files and logs client requests. It reads configuration data from a `config.json` file and provides customization options for port, log output, and allowed file types.

## Features ✨

- **Serve Static Files**: Serves files from the server's directory.
- **Configuration File**: Configurable through a `config.json` file.
- **Logging**: Logs client IP addresses and messages to a file.
- **Customizable**: Change port, index file, and allowed file types.

## Usage 🚀

### 1. Create a Configuration File 📄

Create a `config.json` file in the same directory as your script with the following structure:

```json
{
    "port": 8080,
    "index": "index.html",
    "log": true,
    "output": "log.txt",
    "welcome_message": "HTTP server has joined!",
    "allowed_extensions": {
        ".html": "text/html",
        ".jpg": "image/jpg",
        ".png": "image/png",
        ".txt": "text/plain",
        ".exe": "application/octet-stream",
        ".css": "text/css",
        ".js": "application/javascript"
    }
}
```
## 2. Run the Server 🚀

Run the script using Python:

```bash
python main.py
```

Run the script using bash files:
  - Run the Lib_Installer.bat and install libarys
  - Run the start.bat 

## 3. Access the Server 🌐

Open a web browser and navigate to `http://localhost:PORT`, where `PORT` is the port number specified in `config.json`.

### Example Configuration

- **Port**: 8080
- **Index File**: `index.html`
- **Log File**: `log.txt`
- **Allowed Extensions**: `.html`, `.jpg`, `.png`, `.txt`, `.css`, `.js`

## 4. Modify Configuration 🔄

Update the `config.json` file to change settings such as port number, index file, log file location, and allowed file extensions.

## Requirements 🛠️

- **Python 3**: Ensure Python 3 is installed and properly configured on your system.
- **colorama**: Used for colored text in the terminal.

You can install it with the following command:

```bash
pip install colorama
```

### Note ❗
**This script is designed to run with Python and does not support execution of PHP, Node.js, or other similar server-side scripting languages.**
