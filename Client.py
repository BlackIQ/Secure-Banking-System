import socket
import time

class Client:
	def __init__(self):
		self.Exit = 0
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
		message = self.s.recv(1024).decode()
		self.receive_message(message)

		while True:
			if self.Exit == 1:
				break
			message = input('Secure Banking System> ')
			self.send_message(message)
			while True:
				message = self.s.recv(4096).decode()
				self.receive_message(message)
				break

	def send_message(self,message):
		self.s.send(message.encode())

	def receive_message(self,message):
		if message == "Goodbye.":
			print(message)
			self.Exit = 1
		else:
			print(message)


client = Client()
