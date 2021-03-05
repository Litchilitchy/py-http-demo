from http.server import BaseHTTPRequestHandler
from routes import routes
import logging


logging.basicConfig(level=logging.DEBUG)


class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_GET(self):
        self.respond()

    def do_POST(self):
        logging.info(self.headers['Content-Length'])
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.wfile.write(body)

    def handle_http(self, status, content_type):
        self.send_response(status)
        self.send_header('Content - type', content_type)
        self.end_headers()
        route_content = routes[self.path]
        return bytes(route_content, 'UTF - 8')

    def respond(self):
        content = self.handle_http(200, 'text / html')
        self.wfile.write(content)