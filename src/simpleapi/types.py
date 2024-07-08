import json
import re
from typing import AnyStr, Callable

class Response():
    def __init__(self) -> None:
        self.content_type: str = "text/plain"
        self.status_code: int = 200
        self.content: AnyStr = ""
    
    def set_status(self, code: int):
        self.status_code = code

    def set_json(self, body):
        self.content_type = "application/json"
        self.content = bytes(json.dumps(body), "utf-8")

    def set_text(self, body):
        self.content = bytes(body, "utf-8")

    def apply_to_handler(self, h):
        h.send_response(self.status_code)
        h.send_header("Content-Type", self.content_type)
        h.end_headers()
        h.wfile.write(self.content)


class Router():
    def __init__(self):
        self.routes: dict[re.Pattern, dict[str, Callable]]= {}

    def match(self, method, path):
        for pattern, methods in self.routes.items():
            if pattern.match(path):
                handler = methods.get(method)
                return handler

    def register_handler(self, method, path, handler):
        path_pattern = re.sub(r':(\w+)', r'(?P<\1>[^/]+)', path)
        path_pattern = re.compile(f'^{path_pattern}$')
        if not path_pattern in self.routes:
            self.routes.update({path_pattern: dict()})
        methods: dict = self.routes[path_pattern]
        if not method in methods:
            methods.update({method:handler})
    
    def get(self, path):
        def wrapper(handler):
            self.register_handler("GET", path, handler)
    
        return wrapper

    def post(self, path):
        def wrapper(handler):
            self.register_handler("GET", path, handler)
    
        return wrapper
    
    def __str__(self) -> str:
        routes = self.routes
        return "Router<%a>" % {
            path: methods
            for path, methods in routes.items()
        }
