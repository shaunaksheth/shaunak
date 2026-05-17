import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

HOST = 'localhost'
PORT = 8000

# Hardcoded credentials for the demo
VALID_USERNAME = 'user1'
VALID_PASSWORD = 'Password123'

class LoginHandler(SimpleHTTPRequestHandler):
    def _set_cors_headers(self):
        """Set CORS headers to allow Angular frontend access"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        """Handle preflight CORS requests"""
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path != '/login':
            self.send_error(404, 'Not Found')
            return

        length = int(self.headers.get('Content-Length', '0'))
        body = self.rfile.read(length).decode('utf-8')

        try:
            data = json.loads(body)
            username = data.get('username', '')
            password = data.get('password', '')
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self._set_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': 'Invalid JSON payload.'}).encode('utf-8'))
            return

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            response = {'success': True}
            self.send_response(200)
        else:
            response = {'success': False, 'error': 'Invalid username or password.'}
            self.send_response(401)

        self.send_header('Content-Type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def log_message(self, format, *args):
        # Disable logging for clarity
        return

if __name__ == '__main__':
    server_address = (HOST, PORT)
    handler_class = LoginHandler
    print(f'Serving login API at http://{HOST}:{PORT}')
    print(f'Login endpoint: http://{HOST}:{PORT}/login')
    print(f'\nNote: Run Angular app with: ng serve')
    print(f'Angular app will be at: http://localhost:4200')
    httpd = HTTPServer(server_address, handler_class)
    httpd.serve_forever()
