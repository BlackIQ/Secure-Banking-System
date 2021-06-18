import socket

class Server:
	def __init__(self):
		self.start_server()

	def start_server(self):
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		host = socket.gethostbyname(socket.gethostname())
		port = 12345

		self.clients = []
		self.s.bind((host,port))
		self.s.listen(100)

		print("Running on host: "+str(host))
		print("Running on port: "+str(port))

		while True:
			c, addr = self.s.accept()
			username = c.recv(1024).decode()

			print("New connection. Username: "+str(username))
			self.message = "Your username is " + username
			c.send(self.message.encode())
			print("Server:", self.message)
			break

		self.s.close()

server = Server()
