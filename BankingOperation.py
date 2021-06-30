from MysqlConnection import MysqlConnection

class BankingOperation:
    
    def __init__(self, MysqlConnection):
        self.MysqlConnection=MysqlConnection
    
    def create_account (self, username, account_type, amount, conf_label, integrity_label):
        self.MysqlConnection.mysql_connection()
        account_no = self.MysqlConnection.create_new_account(username, account_type, amount, conf_label, integrity_label)
        response = f"Account Created Successsfully. Your Account Number is: {account_no}"
        self.MysqlConnection.close_connection()
        return response
    