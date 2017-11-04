import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class WSHandler(tornado.websocket.WebSocketHandler):
	def check_origin(self, origin):
		return True

	def open(self):
		print 'Connection opened...'

	def on_message(self, message):
		print 'received :', message

	def on_close(self):
		print 'Connection closed...'

application = tornado.web.Application([
	(r'/', MainHandler)
	(r'/ws', WSHandler)
])

if __name__ == "__main__":
	application.listen(8000)
	tornado.ioloop.IOLoop.instance().start()		

	print('coucou tornado')