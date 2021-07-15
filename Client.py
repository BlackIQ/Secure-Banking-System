import socket
import time
from Cryptography import Encryption_Decryption, Sign_Verify, Private_Keys
from Symmetric_Cryptography import Symmetric_Cryptography
from Crypto.Hash import SHA256
import functools
import operator

class Client:
    def __init__(self):
        self.Exit = 0
        self.symmetric_key = b'b'
        self.check_bytes = b'check'
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
        print(message)
        self.set_session_key()
        while True:
            if self.Exit == 1:
                break
            message = input('Secure Banking System> ')
            self.send_message(message)
            while True:
                message = self.s.recv(4096)
                self.receive_message(message)
                break

    def send_message(self, message):
        if type(self.check_bytes) == type(message):
            msg_secure = Symmetric_Cryptography.symmetric_encryption(message, self.symmetric_key)
            self.s.send(msg_secure)
        else:
            message = message.encode('ascii')
            msg_secure = Symmetric_Cryptography.symmetric_encryption(message, self.symmetric_key)
            self.s.send(msg_secure)

    def receive_message(self, message):
        decrypt_msg = Symmetric_Cryptography.symmetric_decryption(message, self.symmetric_key)
        if decrypt_msg == "Goodbye.":
            print(decrypt_msg)
            self.Exit = 1
        else:
            print(decrypt_msg)

    def set_session_key(self):
        self.symmetric_key = Symmetric_Cryptography.key_generation()
        signed_key, self.symmetric_key = Sign_Verify.sign_client_private_key(self.symmetric_key)
        signed_key_int = functools.reduce(operator.add, signed_key)
        signed_key_bytes = bytes(signed_key_int)
        digested_key = Symmetric_Cryptography.my_hash(signed_key_bytes)
        send_to_server = self.symmetric_key + digested_key
        secure_key_to_server = Encryption_Decryption.encryption_server_public_key(send_to_server)
        self.s.send(secure_key_to_server)
        print("Secure Connection")


client = Client()

