import os

from http.server import BaseHTTPRequestHandler, HTTPServer

from . import mimetypes, file_utils


ROOT_PATH = os.path.abspath(os.getcwd())

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path is '/':
            self.path = '/index.html'

        try:
            mime = mimetypes.get_mimetype(self.path)

            if mime is None:
                self.send_error(500, 'Mimetype not supported: %s' % ROOT_PATH + self.path)
            else:
                _file = file_utils.getFileBytes(ROOT_PATH + self.path, mime['read_type'])

                if _file is not None:
                    self.send_response(200)
                    self.send_header('Content-type', mime['mimetype'])
                    self.end_headers()

                    self.wfile.write(_file)
                else:
                    self.send_error(404, 'File not found: %s', % self.path)

            return
            


def run(port=9000):
    try:
        server = HTTPServer(('127.0.0.1', port), RequestHandler)
        print(
            """
            *******************************
            **                           **
            **          PyServe          **
            **   http://127.0.0.1:%s   **
            **                           **
            *******************************
            """ % port
        )
        server.serve_forever()
    except KeyboardInterrupt:
        print('Shutting down the server')
        server.socket.close()
