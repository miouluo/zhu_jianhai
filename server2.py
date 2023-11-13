import urllib
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
msglist = []
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.requestline)
        self.send_response(200)
        self.send_header("Content-type", "text/html;charset=utf-8")
        self.end_headers()
        f = open('index.html', 'r', encoding='utf-8')
        html = f.read()
        html = html.replace('<%msg%>', self.msg2str())
        f.close()
        self.wfile.write(html.encode('utf-8'))
    def msg2str(self):
        s = ''
        for msg in msglist:
            s += '<p>%s</p ><hr/>'%msg
        return s

    def do_POST(self):
        length = int(self.headers['content-length'])
        qs = self.rfile.read(length)
        txt = urllib.parse.unquote(qs.decode('utf-8'))
        msglist.append(txt)
        self.do_GET()
        print(txt)
if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), MyHandler)
    print(server, '服务器已启动！')
    server.serve_forever()