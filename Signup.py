
class Signup:
    def signup(self, username, password):
        response = "hi from login, your username and password is:" + username + password
        return response
        # tekrari nabodane username ro bayad check kone
            # age tekrari bod etela bede
        # zaeif bodane passwordo bayad check kone
            # age zaeif bod etela bede ke zaeife
            # age zaeif nabod bege sabt shodi
                # to in halat bayad salt ro tolid kone.
                # bayad password ro ba salt jam kone va hash begire
                # bayad insert kone to database
