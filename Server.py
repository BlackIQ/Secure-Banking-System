import socket
from Login import Login

class Server:
	def __init__(self,Login):
		self.Login = Login
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
			self.send_message("Successfully connected. \nYou can use help command for more information.")
			break

		while True:
			msg = self.c1.recv(4096).decode()
			self.receive_message(msg)

	def send_message(self,message):
		self.c1.send(message.encode())
		print("Successfully sent")

	def receive_message(self,message):
		print("message:", message)

		if message == "Help" or message == "help":
			self.send_message("Signup [username] [password]\nLogin [username] [password]")
		elif message == "Signup" or message == "signup":
			# redirect to the corresponding class
			msg = "response from server. your message was:" + message
			self.send_message(msg)
		elif message == "Login" or message == "login":
			# redirect to the corresponding class
			response = self.Login.login("1")
			msg = "response from server. your message was:" + message
			self.send_message(response)
		else:
			self.send_message("Please use help command")


server = Server(Login())
