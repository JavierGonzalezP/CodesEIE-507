import http.server
import socketserver
import ssl

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   certfile="./server.crt",
                                   keyfile="./server.key",
                                   server_side=True)
    httpd.serve_forever()