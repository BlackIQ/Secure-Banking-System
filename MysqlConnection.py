import mysql.connector
from mysql.connector import errorcode

class MysqlConnection:
	def __init__(self):
		self.mysql_connection()
		self.cnx
		self.cursor

	def mysql_connection(self):
		self.cnx = mysql.connector.connect(user='root', password='10101010',
		                              host='127.0.0.1',
		                              database='secure_banking_system')
		self.cursor = self.cnx.cursor(buffered=True)

	def check_username(self, username):
		self.cursor.execute(
			"SELECT * FROM users WHERE username = %s",
			(username,)
		)
		results = self.cursor.fetchall()
		row_count = self.cursor.rowcount
		if row_count == 0:
			return 1
		else:
			return 0

	def insert_into_table(self, username, password_hash, salt, confidentiality_level, integrity_level, number_of_attempts, is_block):
		self.cursor.execute('INSERT INTO users(username, password_hash, salt, confidentiality_level, integrity_level, number_of_attempts, is_block) VALUES(\'%s\',\'%s\',\'%s\',1,1,0,0);' %(username, password_hash, salt))
		self.cnx.commit()

	def fetch_hash_and_salt(self, username):
		self.cursor.execute(
			"select password_hash, salt from users where username = %s",
			(username,)
		)
		results = self.cursor.fetchall()
		return results

	def fetch_block_information(self, username):
		self.cursor.execute(
			"select number_of_attempts, is_block from users where username = %s",
			(username,)
		)
		results = self.cursor.fetchall()
		return results

	def increase_number_of_attempts_and_is_block(self, username):
		self.cursor.execute(
			"select number_of_attempts, is_block from users where username = %s",
			(username,)
		)
		results = self.cursor.fetchall()

		for i in results:
			result = i

		number_of_attempts , is_block = result

		if number_of_attempts == 2:
			self.cursor.execute('update users set  number_of_attempts = number_of_attempts +1, is_block = is_block +1 where username= \'%s\';' %(username, ))
			self.cnx.commit()
		else:
			self.cursor.execute('update users set  number_of_attempts = number_of_attempts +1 where username= \'%s\';' %(username, ))
			self.cnx.commit()

	def reset_number_of_attempts_and_is_block(self, username):

		self.cursor.execute('update users set number_of_attempts = 0 where username= \'%s\';' %(username, ))
		self.cnx.commit()

		self.cursor.execute('update users set is_block = 0 where username= \'%s\';' %(username, ))
		self.cnx.commit()


	def close_connection(self):
		self.cursor.close()
		self.cnx.close()
  
	def create_new_account(self,username,account_type,amount,conf_label,integrity_label):
		self.cursor.execute("select ID from users where username = %s",(username,))
		ids = self.cursor.fetchone()
		user_id = ids[0]
		self.cursor.execute('INSERT INTO accounts(owner_id, account_type_id, amount, confidentiality_level, integrity_level) VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');' %(user_id, account_type, amount, conf_label, integrity_label,))
		self.cnx.commit()
		self.cursor.execute("select account_no from accounts where owner_id = %s and account_type_id = %s and amount = %s and confidentiality_level = %s and integrity_level = %s",(user_id, account_type, amount, conf_label, integrity_label,))
		nos = self.cursor.fetchone()
		account_no=nos[0]
		return account_no

	def add_join_request(self,username, account_no):
		self.cursor.execute("select ID from users where username = %s",(username,))
		ids = self.cursor.fetchone()
		user_id = ids[0]
		self.cursor.execute('select accept_status from account_user where account_no = %s and user_id = %s',(account_no,user_id))
		prev = self.cursor.fetchall()
		response=''
		if len(prev)!=0:
			if prev[0]==1:
				response = f"You Have Already Joint This Account."
			else:
				response = f"You Have Already Requested to Join This Account."

		else :
			self.cursor.execute('Insert into account_user(account_no, user_id) VALUES (\'%s\',\'%s\');' %(account_no,user_id,))
			self.cnx.commit()
			response = f"Join Request Sent to Account Owner."

		return response

	def accept_join_request(self, owner, username, conf_label, integrity_label):
		self.cursor.execute("select ID from users where username = %s",(owner,))
		oids = self.cursor.fetchone()
		owner_id = oids[0]
		self.cursor.execute("select ID from users where username = %s",(username,))
		uids = self.cursor.fetchone()
		user_id = uids[0]
		self.cursor.execute("select account_no from accounts where owner_id = %s",(owner_id,))
		nos = self.cursor.fetchone()
		account_no = nos[0]
		self.cursor.execute('update account_user set accept_status = 1, confidentiality_level = %s, integrity_level = %s where  account_no = %s and user_id = %s',(conf_label,integrity_label, account_no,user_id))
		self.cnx.commit()
		response = f"User \033[1m{username}\033[0m Joint to Account \033[1m{account_no}\033[0m. "
		return response


		
	def show_list_of_account(self, username):
		self.cursor.execute("select ID from users where username = %s",(username,))
		uids = self.cursor.fetchone()
		user_id = uids[0]
		self.cursor.execute("select account_no from accounts where owner_id = %s",(user_id,))
		nos = self.cursor.fetchone()
		account_no = nos[0]
		self.cursor.execute("select account_no from account_user where user_id = %s and accept_status = 1",(user_id,))
		joints = self.cursor.fetchall()
		return account_no, joints

	def account_info(self, username, account_no):
		self.cursor.execute("select ID from users where username = %s",(username,))
		uids = self.cursor.fetchone()
		user_id = uids[0]
		query1 = """select users.username,accounts.DateCreated,accounts.amount,account_type.title
					from accounts inner join users on accounts.owner_id = users.ID 
					inner join account_type on account_type.ID = accounts.account_type_id
					where accounts.account_no = %s"""
		self.cursor.execute(query1,(account_no,))
		account_info = self.cursor.fetchone()
		query2 = """select users.username
					from account_user inner join users on account_user.user_id = users.ID 
					where account_user.account_no = %s and account_user.accept_status = 1"""
		self.cursor.execute(query2,(account_no,))
		owners =  self.cursor.fetchall()
		query3 = """select *
					from transactions 
					where from_account = %s order by transaction_date DESC limit 5"""
		self.cursor.execute(query3,(account_no,))
		last5_deposits = self.cursor.fetchall()
		query4 = """select *
					from transactions 
					where to_account = %s order by transaction_date DESC limit 5"""
		self.cursor.execute(query4,(account_no,))
		last5_withdraw = self.cursor.fetchall()

		return account_info,owners,last5_deposits,last5_withdraw



     

    