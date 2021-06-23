import base64
import os
import hashlib
from MysqlConnection import MysqlConnection
import re

class Login:
    def __init__(self, MysqlConnection):
        self.MysqlConnection = MysqlConnection

    def login(self, username, password):
        valid_username = self.MysqlConnection.check_username(username)

        if valid_username == 1:
            response = "This username does not exist."
        else:
            correct_password = self.check_the_input_password(password, username)
            if correct_password == 0:
                response = "The input password is incorrect."
                #backoff should increase here
            else:
                response = "You have successfully Logged in. You can use help command for more information."

        return response

    def check_the_input_password(self, password, username):
        hash_and_salt = self.MysqlConnection.fetch_hash_and_salt(username, password)

        for i in hash_and_salt:
            result = i
        hash , salt = result

        passwordWithSalt = salt + password

        m = hashlib.sha256()
        m.update(passwordWithSalt.encode())
        input_password_hash = m.hexdigest()

        if input_password_hash == hash:
            correct_password = 1
        else:
            correct_password = 0

        return correct_password

        # bar asase username vorodi, az database salt va hash ro select koni (DONE)
            # agar username vojod nadasht error bede (DONE)
            # salt ro + password vorodi koni hash begiri va compare koni
                # agar dorost bod bege ok
                    # state system ro avaz kone
                # agar ghalat bod error bede
            # piade sazi mechanisme backoff
            # piade sazi honeypot
