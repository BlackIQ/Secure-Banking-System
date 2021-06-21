import base64
import os
import hashlib
from MysqlConnection import MysqlConnection

class Signup:
    def __init__(self, MysqlConnection):
        self.MysqlConnection = MysqlConnection

    def base64_encode(self, message_bytes):
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message

    def signup(self, username, password):
        salt = self.base64_encode(os.urandom(12)) #Generate 12 bytes salt
        passwordWithSalt = salt + password

        m = hashlib.sha256()
        m.update(passwordWithSalt.encode())
        password_hash = m.hexdigest()

        status = self.MysqlConnection.insert_into_table(username, password_hash, salt, 1, 1, 1, "NULL", 0)

        if status == 1:
            response = "Singup Successfully"
        if status == 0:
            response = "This username exists. Please select another username."


        return response


        # tekrari nabodane username ro bayad check kone () (DONE)
            # age tekrari bod etela bede () (DONE)
        # zaeif bodane passwordo bayad check kone ()
            # age zaeif bod etela bede ke zaeife ()
            # age zaeif nabod bege sabt shodi ()
                # to in halat bayad salt ro tolid kone. (DONE)
                # bayad password ro ba salt jam kone va hash begire (DONE)
                # bayad insert kone to database (DONE)
