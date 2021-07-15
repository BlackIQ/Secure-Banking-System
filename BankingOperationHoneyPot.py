from MysqlConnection import MysqlConnection

class BankingOperationHoneyPot:

    def __init__(self, MysqlConnection):
        self.MysqlConnection = MysqlConnection

    def create_account(self, username, account_type, amount, conf_label, integrity_label):
        self.MysqlConnection.mysql_connection()
        response = f"Account Created Successfully. Your Account Number is: 1000001023"
        self.MysqlConnection.record_log(username, 'Create Account', 'honeypot', amount)
        self.MysqlConnection.close_connection()
        return response

    def join(self, username, account_no):
        self.MysqlConnection.mysql_connection()
        response = f"Join Request Sent to Account Owner."
        self.MysqlConnection.record_log(username, 'Join', 'honeypot', None,account_no)
        self.MysqlConnection.close_connection()
        return response

    def accept(self, owner, username, conf_label, integrity_label):
        self.MysqlConnection.mysql_connection()
        response = f"User \033[1m{username}\033[0m Joint to Account \033[1m{1000001023}\033[0m. "
        self.MysqlConnection.record_log(owner, 'Accept', 'honeypot')
        self.MysqlConnection.close_connection()
        return response

    def show_MyAccount(self, username):
        self.MysqlConnection.mysql_connection()
        response = f"1. \033[1m{1000001023}\033[0m\n"
        self.MysqlConnection.record_log(username, 'Show MyAccount', 'honeypot')
        self.MysqlConnection.close_connection()
        return response

    def show_Account(self, username, account_no):  # Access Control Needed.
        self.MysqlConnection.mysql_connection()
        response = f"\n\033[1m Creator:\033[0m {username}\t\033[1m Amount:\033[0m {13212}\n"
        response = response + "\033[1m Owners:\033[0m\n"
        response = response + "\033[1m 5 Most Recent Deposits:\033[0m\n"
        response = response + "\033[1m 5 Most Recent Withdraws:\033[0m\n"
        self.MysqlConnection.record_log(username, 'Show_Account', 'honeypot', None, account_no)
        self.MysqlConnection.close_connection()
        return response

    def deposit(self, owner, to_account, amount):  # Access Control Needed.
        self.MysqlConnection.mysql_connection()
        response = f"Successful Transaction."
        self.MysqlConnection.record_log(owner, 'Deposit', 'honeypot', amount, None, to_account)
        self.MysqlConnection.close_connection()
        return response

    def withdraw(self, username, from_account, to_account, amount):  # Access Control Needed.
        self.MysqlConnection.mysql_connection()
        response = f"Successful Transaction."
        self.MysqlConnection.record_log(username, 'Withdraw', 'honeypot', amount, from_account, to_account)
        self.MysqlConnection.close_connection()
        return response
