from MysqlConnection import MysqlConnection
from AccessControl import AccessControl


class BankingOperation:

    def __init__(self, MysqlConnection, AccessControl):
        self.MysqlConnection = MysqlConnection
        self.AccessControl = AccessControl

    def create_account(self, username, account_type, amount, conf_label, integrity_label):
        self.MysqlConnection.mysql_connection()
        account_no = self.MysqlConnection.create_new_account(username, account_type, amount, conf_label,
                                                             integrity_label)
        response = f"Account Created Successfully. Your Account Number is: {account_no}"
        self.MysqlConnection.record_log(username, 'Create Account', 'Successful', amount)
        self.MysqlConnection.close_connection()
        return response

    def join(self, username, account_no):
        self.MysqlConnection.mysql_connection()
        response = self.MysqlConnection.add_join_request(username, account_no)
        self.MysqlConnection.record_log(username, 'Join', 'Successful', None,account_no)
        self.MysqlConnection.close_connection()
        return response

    def accept(self, owner, username, conf_label, integrity_label):
        self.MysqlConnection.mysql_connection()
        response = self.MysqlConnection.accept_join_request(owner, username, conf_label, integrity_label)
        self.MysqlConnection.record_log(username, 'Accept', 'Successful')
        self.MysqlConnection.close_connection()
        return response

    def show_MyAccount(self, username):
        self.MysqlConnection.mysql_connection()
        account_no, joints = self.MysqlConnection.show_list_of_account(username)
        response = f"1. \033[1m{account_no}\033[0m\n"
        js = ''
        for i in range(2, len(joints) + 2):
            js = js + f"{i}. {joints[i - 2][0]}\n"
        response = response + js
        self.MysqlConnection.record_log(username, 'Show MyAccount', 'Successful')
        self.MysqlConnection.close_connection()
        return response

    def show_Account(self, username, account_no):  # Access Control Needed.
        status, msg = self.AccessControl.has_read_access(username, account_no)

        if status == 1:
            self.MysqlConnection.mysql_connection()
            account_info, owners, last5_deposits, last5_withdraw = self.MysqlConnection.account_info(username,
                                                                                                     account_no)
            response = f"\n\033[1m Creator:\033[0m {account_info[0]}\t\033[1m DateCreated:\033[0m {account_info[1]}\t\033[1m Amount:\033[0m {account_info[2]}\t\033[1m Type:\033[0m {account_info[3]}\n"
            response = response + "\033[1m Owners:\033[0m\n"
            for i in range(0, len(owners)):
                response = response + f"\t{i + 1}. {owners[i][0]}\n"

            response = response + "\033[1m 5 Most Recent Deposits:\033[0m\n"
            for i in range(0, len(last5_deposits)):
                response = response + f"\t{i + 1}. To: {last5_deposits[i][2]}\tAmount: {last5_deposits[i][3]}\tDate: {last5_deposits[i][4]}\n"

            response = response + "\033[1m 5 Most Recent Withdraws:\033[0m\n"
            for i in range(0, len(last5_withdraw)):
                response = response + f"\t{i + 1}. From: {last5_withdraw[i][1]}\tAmount: {last5_withdraw[i][3]}\tDate: {last5_withdraw[i][4]}\n"
            self.MysqlConnection.record_log(username, 'Show_Account', 'Successful', None, account_no)
            self.MysqlConnection.close_connection()
            return response
        else:
            self.MysqlConnection.record_log(username, 'Show_Account', 'fail', None, account_no)
            return msg
        self.MysqlConnection.close_connection()

    def deposit(self, owner, to_account, amount):  # Access Control Needed.
        self.MysqlConnection.mysql_connection()
        response = self.MysqlConnection.deposit_to_account(owner, to_account, amount)
        self.MysqlConnection.record_log(owner, 'Deposit', 'Successful', amount, None, to_account)
        self.MysqlConnection.close_connection()
        return response

    def withdraw(self, username, from_account, to_account, amount):  # Access Control Needed.
        status, msg = self.AccessControl.has_write_access(username, from_account)
        if status == 1:
            self.MysqlConnection.mysql_connection()
            response = self.MysqlConnection.withdraw(username, from_account, to_account, amount)
            self.MysqlConnection.record_log(username, 'Withdraw', 'Successful', amount, from_account, to_account)

            return response
        else:
            self.MysqlConnection.record_log(username, 'Withdraw', 'fail', amount, from_account, to_account)
            return msg

        self.MysqlConnection.close_connection()




