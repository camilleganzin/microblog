import os

from urlparse import urlparse
from django.conf import settings

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.websocket import WebSocketHandler
import tornado.template
import tornado.wsgi
import tornado.httpserver
from tornado.options import define, parse_command_line, options

# from django.shortcuts import redirect

class WSHandler(WebSocketHandler):

	def open(self, socket, data):
		print 'Connection opened...'% socket

	def on_message(self, message, socket, data):
		print 'received :', message

	def on_close(self, socket, data):
		print 'Connection closed...'% socket

application = Application([
	(r'/my_ws', WSHandler),
])
application.listen(8000)
tornado.ioloop.IOLoop.instance().start()




# class MainHandler(tornado.web.RequestHandler):
# 	def get(self):
# 		self.write("Hello, world")
# 		print('coucou')

# class WSHandler(WebSocketHandler):

# 	print WebSocket

# 	@my_ws.on
# 	def open(self, socket, data):
# 		ws_echo.emit('new_connection')
# 		print 'Connection opened...'% socket

# 	@my_ws.on
# 	def on_message(self, message, socket, data):
# 		socket.emit('message', data)
# 		print 'received :', message

# 	@my_ws.on
# 	def on_close(self, socket, data):
# 		ws_echo.emit('closed_connection')
# 		print 'Connection closed...'% socket

# # application = tornado.web.Application([
# # 	(r'/', MainHandler),
# # 	(r'/ws', WSHandler)
# # ])

# application = Application([
# 	(r"/", WSHandler),
# ])

# def simple_app(environ, start_response):
#     status = "200 OK"
#     response_headers = [("Content-type", "text/plain")]
#     start_response(status, response_headers)
#     return redirect('/microblog')

# container = tornado.wsgi.WSGIContainer(application)
# print container
# http_server = tornado.httpserver.HTTPServer(container)
# http_server.listen(8000)
# tornado.ioloop.IOLoop.current().start()
# application.listen(8000)
# tornado.ioloop.IOLoop.instance().start()

# application = Application(
# 	handlers=[
# 	  (r"/", IndexHandler),
# 	  (r"/my_ws", WSHandler)
# 	],
# 	debug = True,
# 	template_path = os.path.join(os.path.dirname(__file__), "templates/microblog"),
# 	static_path = os.path.join(os.path.dirname(__file__), "static")
# )