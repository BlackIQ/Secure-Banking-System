import base64
import os
import hashlib
from MysqlConnection import MysqlConnection
import re

class Signup:
    def __init__(self, MysqlConnection):
        self.MysqlConnection = MysqlConnection

    def base64_encode(self, message_bytes):
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message

    def signup(self, username, password):
        valid_username = self.MysqlConnection.check_username(username)
        valid_password = self.check_password(password, username)

        if valid_username == 0:
            response = "This username exists. Please select another username."
        elif valid_password == 0:
            response = "Your password is short. It needs to be at least 8 characters."
        elif valid_password == -1:
            response = "Your password is weak. Please Use numbers, uppercase and lowercase letters in your password."
        elif valid_password == -2:
            response = "Your password is weak. Password should have at least one of the symbols $ or _ or @"
        elif valid_password == -3:
            response = "Your password is weak. Your password should not contain your username."
        else:
            salt = self.base64_encode(os.urandom(12)) #Generate 12 bytes salt
            passwordWithSalt = salt + password

            m = hashlib.sha256()
            m.update(passwordWithSalt.encode())
            password_hash = m.hexdigest()

            self.MysqlConnection.insert_into_table(username, password_hash, salt, 1, 1, 1, "NULL", 0)

            response = "You have successfully Signed up. Now you can Login."

        return response

    def check_password(self, password, username):
        valid = 1

        if len(password) < 8:
            valid = 0
        elif not re.search("[0-9]", password):
            valid = -1
        elif not re.search("[A-Z]", password):
            valid = -1
        elif not re.search("[a-z]", password):
            valid = -1
        elif not re.search("[$_@]", password):
            valid = -2
        if username in password:
            valid = -3
        return valid
