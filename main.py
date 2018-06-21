
import os

#from werkzeug.wrappers import Request, Response
from flask import Flask, send_from_directory, render_template

from model.db import initialize
from model.api.user import User, user_bp

app = Flask(__name__)
#app = Flask(__name__, static_folder="/view/web/static", template_folder="view/web/static")

'''
@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists('view/web/static/' + path):
        return send_from_directory('view/web/static', path)
    else:
        return send_from_directory('view/web/static', "index.html")
        #return render_template("index.html")
'''


if __name__ == "__main__":
    initialize()

    app.register_blueprint(user_bp)
    app.run("0.0.0.0", 8000)





'''
class WallFlower(object):
    def dispatch_request(self, request):
        with open("view/web/index.html") as f:
            return Response(f.read(), mimetype='text/html')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(host='0.0.0.0', port=8000):
    app = WallFlower()
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/deps': os.path.join(os.path.dirname(__file__), "view/web/deps")
        '/js': os.path.join(os.path.dirname(__file__), "view/web/js")
    })

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 8000, create_app)
'''

''' Python 2.7 httpserver
import SimpleHTTPServer
import SocketServer

PORT = 8000

if __name__ == "__main__":
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    httpd.serve_forever()
'''


