import socket
from Login import Login
from Signup import Signup
from MysqlConnection import MysqlConnection

class Server:
	def __init__(self, Login, Signup, MysqlConnection):
		self.Exit = 0
		self.Login = Login
		self.Signup = Signup
		self.MysqlConnection = MysqlConnection
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
			if self.Exit == 1:
				self.send_message("Goodbye.")
				break
			msg = self.c1.recv(4096).decode()
			self.receive_message(msg)

		self.MysqlConnection.close_connection()
		self.s.close()

	def send_message(self,message):
		self.c1.send(message.encode())
		print("Successfully sent")

	def receive_message(self, inputCommand):
		print("Input command:", inputCommand)

		Parts = inputCommand.split()

		if Parts[0] == "Help" or Parts[0] == "help":
			self.send_message("Signup [username] [password]\nLogin [username] [password]\nExit")

		elif Parts[0] == "Signup" or Parts[0] == "signup":
			if len(Parts) == 3:
				response = self.Signup.signup(Parts[1], Parts[2])
				self.send_message(response)
			else:
				self.send_message("Incorrect arguments. Please use help command")

		elif Parts[0] == "Login" or Parts[0] == "login":
			if len(Parts) == 3:
				response = self.Login.login(Parts[1], Parts[2])
				self.send_message(response)
			else:
				self.send_message("Incorrect arguments. Please use help command")

		elif Parts[0] == "Exit" or Parts[0] == "exit":
			self.Exit = 1

		else:
			self.send_message("Please use help command")


server = Server(Login(),Signup(MysqlConnection()),MysqlConnection())
