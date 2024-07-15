from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import json
import os
from colorama import init, Fore, Style

# JSON dosyası yolu ve verileri okuma
json_path = './config.json'
with open(json_path, 'r') as file:
    data = json.load(file)

# Config verilerini değişkenlere atama
port = data.get("port", 8080)
index_path = data.get("index", "index.html")
log_enabled = data.get("log", True)
output_log = data.get("output", "log.txt")
welcome_message = data.get("welcome_message", "HTTP server has joined!")
allowed_extensions = data.get("allowed_extensions", {
    ".html": "text/html",
    ".jpg": "image/jpg",
    ".png": "image/png",
    ".txt": "text/plain",
    ".exe": "application/octet-stream",
    ".css": "text/css",
    ".js": "application/javascript"
})

# Sunucu bilgileri
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

# Bağlantı bilgileri
connection = f"{ip_address}:{port}"

# Loglama fonksiyonu
def log_message(client_ip, message):
    print(f"\n[+]Logined IP Address: {client_ip} - {message}")
    if log_enabled:
        with open(output_log, "a") as dosya:
            dosya.write(f"\n[+]IP Address: {client_ip} - {message}")

# HTTP Server işleyicisi sınıfı
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/':
                self.path = '/' + index_path  # Varsayılan olarak index.html'i göster
            
            ext = os.path.splitext(self.path)[1]
            mimetype = 'application/octet-stream'
            
            if ext in allowed_extensions:
                mimetype = allowed_extensions[ext]
            else:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b'403: Forbidden')
                return
            
            with open(self.path[1:], 'rb') as f:
                content = f.read()
                
            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            self.wfile.write(content)
        
        except Exception as e:
            print(f"Hata: {e}")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'500: Internal Server Error')

# Başlangıç mesajları
init(autoreset=True)
print(Fore.WHITE + Style.DIM + "HTTP SERVER IS STARTING" + Style.RESET_ALL)
if log_enabled:
    print(f"Output: true, File Path: {output_log}")

print(Fore.GREEN + Style.BRIGHT + "HTTP Server is Running!" + Fore.RESET,
      f"| {Fore.CYAN}Details:\n Port: {port}\n Address: {ip_address}\n Connection: {connection}\n Welcome Message: {welcome_message}")

print(Fore.LIGHTYELLOW_EX)
try:
    # HTTP sunucusunu başlatma
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
except Exception as ex:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Style.BRIGHT + Fore.RED + "HTTP SERVER IS CLOSING" + Fore.RESET + Style.RESET_ALL)
