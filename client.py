import socket

class Client:
	def __init__(self):
		self.create_connection()

	def create_connection(self):
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		while 1:
			try:
				host = input('Enter host name --> ')
				port = 12345
				self.s.connect((host,port))

				break
			except:
				print("Couldn't connect to server")

		self.username = input('Enter username --> ')
		self.s.send(self.username.encode()) #Sending username for server

		message = self.s.recv(1024).decode()
		print("Server:",message)

client = Client()
