from CodinCloud import app as ide_instance
app = ide_instance.app

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import os

PORT = int(os.environ.get("PORT",5000))

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(PORT)
print("Serving CodinCloud on {}".format(PORT))
IOLoop.instance().start()
