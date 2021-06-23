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
        correct_password = self.check_the_input_password(password, username)

        if valid_username == 1:
            response = "This username does not exist."
        elif correct_password == 1:
            response = "You have successfully Logged in. You can use help command for more information."

        return response

    def check_the_input_password(self, password, username):
        correct_password = 1
        return correct_password

        # bar asase username vorodi, az database salt va hash ro select koni
            # agar username vojod nadasht error bede
            # salt ro + password vorodi koni hash begiri va compare koni
                # agar dorost bod bege ok
                    # state system ro avaz kone
                # agar ghalat bod error bede
            # piade sazi mechanisme backoff
            # piade sazi honeypot
