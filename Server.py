import http.server
import json
import core.TScraper


class _Handler(http.server.SimpleHTTPRequestHandler):
    index_file = open('index.html')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        command = json.loads(post_data)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("hello Glu".encode())
        self.process_command(command)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        _Handler.index_file.seek(0)
        self.wfile.write(_Handler.index_file.read().encode())

    def process_command(self, cmd):
        id = cmd['id']
        if cmd['type'] == 'scrap':
            if cmd['level'] == 'forum':
                core.TScraper.scrap_forum(id)
            elif cmd['level'] == 'topic':
                core.TScraper.scrap_topic(id)
        elif cmd['type'] == 'parse':
            pass


server_address = ('', 7777)
httpd = http.server.HTTPServer(server_address, _Handler)
httpd.serve_forever()
