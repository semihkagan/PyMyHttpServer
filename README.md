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
