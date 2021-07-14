import socket
from Login import Login
from Signup import Signup
from MysqlConnection import MysqlConnection
from BankingOperation import BankingOperation
import time

class Server:
	def __init__(self, Login, Signup, MysqlConnection, BankingOperation):
		self.Exit = 0
		self.state = 0
		self.Login = Login
		self.Signup = Signup
		self.MysqlConnection = MysqlConnection
		self.BankingOperation = BankingOperation
		self.start_server()
		self.c1
		self.username=''

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
			if self.state == 1:
				self.receive_message_state_1(msg)
			else:
				self.receive_message_state_0(msg)

		self.s.close()

	def send_message(self,message):
		self.c1.send(message.encode())
		print("Successfully sent")

	def receive_message_state_0(self, inputCommand):
		print("Input command:", inputCommand)

		Parts = inputCommand.split()

		if Parts[0] == "Help" or Parts[0] == "help":
			self.send_message("\nSignup [username] [password]\nLogin [username] [password]\nExit\n")

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
				if "Logged in" in response:
					self.state = 1
					self.username = Parts[1]
					# self.password = Parts[2]
				if "1" in response:
					time.sleep(60) # delays for 1 minute
				elif "2" in response:
					time.sleep(120) # delays for 2 minutes
				elif "4" in response:
					time.sleep(240) # delays for 4 minutes
			else:
				self.send_message("Incorrect arguments. Please use help command")

		elif Parts[0] == "Exit" or Parts[0] == "exit":
			self.Exit = 1

		else:
			self.send_message("Please use help command")

	def receive_message_state_1(self, inputCommand): #this state is for Banking Operations
		print("Input command:", inputCommand)

		Parts = inputCommand.split()

		if Parts[0] == "Help" or Parts[0] == "help":
			self.send_message("""\nCreate [account_type] [amount] [conf_label] [integrity_label]\n\t 
[account_type] : \n\t\t1:Short-term deposit\n\t\t2:Long-term deposit\n\t\t3:Current\n\t\t4:Interest-free\n\t
[conf_label] : \n\t\t1:Unclassified\n\t\t2:Confidential\n\t\t3:Secret\n\t\t4:Top Secret\n\t
[integrity_label] : \n\t\t1:UnTrusted\n\t\t2:SlightlyTrusted\n\t\t3:Trusted\n\t\t4:VeryTrusted\n
Join [account_no]
Accept [username] [conf_label] [integrity_label]
Show_MyAccount
Show_Account [account_no]
Deposit  [to_account_no] [amount]
Withdraw [from_account_no] [to_account_no] [amount]
Exit\n""")

		elif Parts[0] == "Create" or Parts[0] == "create":
			if len(Parts) == 5:
				response = self.BankingOperation.create_account(self.username, Parts[1], Parts[2], Parts[3], Parts[4])
				self.send_message(response)
			else:
				self.send_message("Incorrect arguments. Please use help command")

		elif Parts[0] == "Join" or Parts[0] == "join":
			if len(Parts) == 2:
				response = self.BankingOperation.join(self.username, Parts[1])
				self.send_message(response)
			else:
				self.send_message("Incorrect arguments. Please use help command")

		elif Parts[0] == "Accept" or Parts[0] == "accept":
			if len(Parts) == 4:
				response = self.BankingOperation.accept(self.username, Parts[1], Parts[2], Parts[3])
				self.send_message(response)
			else:
				self.send_message("Incorrect arguments. Please use help command")

		elif Parts[0] == "Show_MyAccount" or Parts[0] == "show_MyAccount":
			if len(Parts) == 1:
				response = self.BankingOperation.show_MyAccount(self.username)
				self.send_message(response)
			else:
				self.send_message("Incorrect arguments. Please use help command")

		elif Parts[0] == "show_Account" or Parts[0] == "show_Account":
			if len(Parts) == 2:
				response = self.BankingOperation.show_Account(self.username, Parts[1])
				self.send_message(response)
			else:
				self.send_message("Incorrect arguments. Please use help command")

		elif Parts[0] == "Deposit" or Parts[0] == "deposit":
			if len(Parts) == 3:
				response = self.BankingOperation.deposit(self.username,Parts[1], Parts[2])
				self.send_message(response)
			else:
				self.send_message("Incorrect arguments. Please use help command")

		elif Parts[0] == "Withdraw" or Parts[0] == "withdraw":
			if len(Parts) == 4:
				response = self.BankingOperation.withdraw(self.username, Parts[1], Parts[2], Parts[3])
				self.send_message(response)
			else:
				self.send_message("Incorrect arguments. Please use help command")

		elif Parts[0] == "Exit" or Parts[0] == "exit":
			self.Exit = 1

		else:
			self.send_message("Please use help command")


server = Server(Login(MysqlConnection()),Signup(MysqlConnection()),MysqlConnection(),BankingOperation(MysqlConnection()))
