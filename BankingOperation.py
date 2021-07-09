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
    
    def join (self,username, account_no):
        self.MysqlConnection.mysql_connection()
        response = self.MysqlConnection.add_join_request(username,account_no)
        self.MysqlConnection.close_connection()
        return response
    
    def accept (self, owner, username,conf_label, integrity_label):
        self.MysqlConnection.mysql_connection()
        response = self.MysqlConnection.accept_join_request(owner,username, conf_label,integrity_label)
        self.MysqlConnection.close_connection()
        return response
    
    def show_MyAccount(self, username):
        self.MysqlConnection.mysql_connection()
        account_no, joints = self.MysqlConnection.show_list_of_account(username)
        response = f"1. \033[1m{account_no}\03show3[0m\n"
        js = ''
        for i in range(2,len(joints)+2):
            js = js + f"{i}. {joints[i-2][0]}\n"
        response = response + js 
        self.MysqlConnection.close_connection()
        return response
    
        