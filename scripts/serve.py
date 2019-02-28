#! python
# -*- encoding:utf-8 -*-

import os, subprocess

from http.server import HTTPServer, BaseHTTPRequestHandler


class ServeApp(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path is '/':
            self.path = '/index.html'
        
        valid_file = False
        if self.path.endswith('.html'):
            mimetype = 'text/html'
            read_type = 'r'
            valid_file = True

        if self.path.endswith('.css'):
            mimetype = 'text/css'
            read_type = 'r'
            valid_file = True

        if self.path.endswith('.js'):
            mimetype = 'application/js'
            read_type = 'r'
            valid_file = True

        if self.path.endswith('.png'):
            mimetype = 'image/png'
            read_type = 'rb'
            valid_file = True

        if self.path.endswith('.jpg'):
            mimetype = 'image/jpg'
            read_type = 'rb'
            valid_file = True

        if self.path.endswith('.ico'):
            mimetype = 'image/x-icon'
            read_type = 'rb'
            valid_file = True

        if self.path.endswith('.gif'):
            mimetype = 'image/gif'
            read_type = 'rb'
            valid_file = True

        if valid_file is True:
            root_path = os.path.abspath(os.getcwd())
            absfilepth = root_path + self.path 
            
            try:
                _file = open(absfilepth, read_type)
            except:
                self.send_error(404, 'File not found: %s' % self.path)
                return

            _file_content = _file.read()

            if not type(_file_content) is bytes:
                _file_content = _file_content.encode('utf-8')

            # Send status 200
            self.send_response(200)
            
            # response content-type header
            self.send_header('Content-type', mimetype + '; charset=utf-8')
            self.end_headers()

            # Return the contents of the file on response
            self.wfile.write(_file_content)

        else:
            return self.send_error(404, 'File not found: %s' % filepath)
        return


if __name__ == '__main__':
    HOST = subprocess.check_output(['hostname', '--all-ip-addresses']) 
    HOST = HOST.decode('utf-8').replace('\n', '')
    PORT = 5000
    SERVER = HTTPServer(('0.0.0.0', PORT), ServeApp)

    try:
        print(' [*] Local %s:%i' % ('127.0.0.1', PORT))
        print(' [*] External %s:%i' % (HOST, PORT))
        SERVER.serve_forever()
    except KeyboardInterrupt:
        print('\n [*] Shutting down the server')
        SERVER.socket.close()
