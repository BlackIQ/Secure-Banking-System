import base64
import os
import hashlib
from MysqlConnection import MysqlConnection
import re


class Login:
    def __init__(self, MysqlConnection):
        self.MysqlConnection = MysqlConnection

    def login(self, username, password):
        self.MysqlConnection.mysql_connection()
        valid_username = self.MysqlConnection.check_username(username)

        if valid_username == 1:
            response = "This username does not exist. If you don't have an account, you need to signup."
            self.MysqlConnection.record_log(username, 'Login', 'fail')
        else:
            block_informaiton = self.backoff_mechanism(username)
            correct_password = self.check_the_input_password(password, username)
            if correct_password == 1:  # password is currect
                response = "You have successfully Logged in. You can use help command for more information."
                self.MysqlConnection.record_log(username, 'Login', 'successful')
                self.MysqlConnection.reset_number_of_attempts_and_is_block(username)
                # go to next state

            elif correct_password == 0:  # password is not currect
                if block_informaiton == 0:  # Account is not block. Attempt number < 3
                    response = "The input password is incorrect."
                    self.MysqlConnection.increase_number_of_attempts_and_is_block(username)
                    self.MysqlConnection.record_log(username, 'Login', 'fail')

                elif block_informaiton == 1:  # Account is block for 1 minute. Attempt number = 3
                    self.MysqlConnection.increase_number_of_attempts_and_is_block(username)
                    response = "The input password is incorrect. Your account is block for 1 minute."
                    self.MysqlConnection.record_log(username, 'Login', 'fail')

                elif block_informaiton == 2:  # Account is block for 2 minutes. Attempt number = 4
                    self.MysqlConnection.increase_number_of_attempts_and_is_block(username)
                    response = "The input password is incorrect. Your account is block for 2 minutes."
                    self.MysqlConnection.record_log(username, 'Login', 'fail')

                elif block_informaiton == 3:  # Account is block for 4 minutes. Attempt number = 5
                    self.MysqlConnection.increase_number_of_attempts_and_is_block(username)
                    response = "The input password is incorrect. Your account is block for 4 minutes."
                    self.MysqlConnection.record_log(username, 'Login', 'fail')

                else:  # Account is block. Attempt number >= 6 => ** Honeypot **
                    response = "Welcome. You have successfully Logged in. You can use help command for more information." ##### HONEYPOT
                    self.MysqlConnection.record_log(username, 'Login', 'honeypot')
                    # honeypot()

        self.MysqlConnection.close_connection()
        return response

    def check_the_input_password(self, password, username):
        hash_and_salt = self.MysqlConnection.fetch_hash_and_salt(username)

        for i in hash_and_salt:
            result = i
        hash, salt = result

        passwordWithSalt = salt + password

        m = hashlib.sha256()
        m.update(passwordWithSalt.encode())
        input_password_hash = m.hexdigest()

        if input_password_hash == hash:
            correct_password = 1
        else:
            correct_password = 0

        return correct_password

    def backoff_mechanism(self, username):
        block_informaiton = self.MysqlConnection.fetch_block_information(username)

        for i in block_informaiton:
            result = i

        number_of_attempts, is_block = result

        block_info = 0

        if is_block == 0 and number_of_attempts < 3:
            block_info = 0
        elif number_of_attempts == 3 and is_block == 1:
            block_info = 1
        elif number_of_attempts == 4 and is_block == 1:
            block_info = 2
        elif number_of_attempts == 5 and is_block == 1:
            block_info = 3
        elif number_of_attempts >= 6 and is_block == 1:
            block_info = 4

        return block_info
