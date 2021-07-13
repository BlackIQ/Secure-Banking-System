import socket
import time
from Cryptography import Encryption_Decryption, Sign_Verify, Private_Keys
from Symmetric_Cryptography import Symmetric_Cryptography
from Crypto.Hash import SHA256

class Client:
    def __init__(self):
        self.Exit = 0
        self.create_connection()

    def create_connection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while 1:
            try:
                host = input('Enter host name --> ')
                port = 12345
                self.s.connect((host, port))

                break
            except:
                print("Couldn't connect to server")
        message = self.s.recv(1024).decode()
        self.receive_message(message)
        symmetric_key = Symmetric_Cryptography.key_generation()
        signed_key, key = Sign_Verify.sign_client_private_key(symmetric_key)
        signed_key_digest = SHA256.new(signed_key)
        secure_signed_key_to_server = Encryption_Decryption.encryption_server_public_key(str(signed_key_digest).encode())
        secure_key_to_server = Encryption_Decryption.encryption_server_public_key(key)
        final_msg = str(secure_signed_key_to_server) + " " + str(secure_key_to_server)
        self.send_message(final_msg)
        while True:
            if self.Exit == 1:
                break
            message = input('Secure Banking System> ')
            self.send_message(message)
            while True:
                message = self.s.recv(4096).decode()
                self.receive_message(message)
                break

    def send_message(self, message):
        self.s.send(message.encode())

    def receive_message(self, message):
        if message == "Goodbye.":
            print(message)
            self.Exit = 1
        else:
            print(message)


client = Client()


