from http import HTTPStatus
from http.server import HTTPServer as BaseHTTPServer, BaseHTTPRequestHandler

from simpleapi.types import Response

class RouterBasedHTTPHandler(BaseHTTPRequestHandler):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.server: RouterBasedHTTPServer

    def handle_one_request(self) -> None:
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
                return
            if not self.raw_requestline:
                self.close_connection = True
                return
            if not self.parse_request():
                # An error code has been sent, just exit
                return
            
            handler = self.server.router.match(self.command, self.path)
            if handler:
                r = Response()
                handler(r)
                r.apply_to_handler(self)
            else:
                self.send_response(404)
                self.end_headers()
            
            self.wfile.flush() #actually send the response if not already done.
        except TimeoutError as e:
            #a read or a write timed out.  Discard this connection
            self.log_error("Request timed out: %r", e)
            self.close_connection = True
            return


class RouterBasedHTTPServer(BaseHTTPServer):
    def __init__(self, server_address, router, bind_and_activate: bool = True) -> None:
        super().__init__(server_address, RouterBasedHTTPHandler, bind_and_activate)
        self.router = router

def start_server(port, router):
    with RouterBasedHTTPServer(('', port), router) as server:
        try:
            print("Server started at port", port)
            server.serve_forever()
        except KeyboardInterrupt:
            pass  

    print("Server closed.")
