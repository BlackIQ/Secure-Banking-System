import socket

class Server:
	def __init__(self):
		self.start_server()
		self.c1
	def start_server(self):
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		host = socket.gethostbyname(socket.gethostname())
		port = 12345

		self.s.bind((host,port))
		self.s.listen(100)

		print("Running on host: "+str(host))
		print("Running on port: "+str(port))

		while True:
			self.c1, addr = self.s.accept()
			username = self.c1.recv(1024).decode()
			print("New connection. Username: "+str(username))
			self.msg = "Your username is " + username
			self.send_message(self.msg)

	def send_message(self,message):
		self.c1.send(message.encode())
		print("Successfully sent")

server = Server()
