import mysql.connector

class MysqlConnection:
	def __init__(self):
		self.mysql_connection()
		self.cnx
		self.cursor

	def mysql_connection(self):
		self.cnx = mysql.connector.connect(user='root', password='10101010',
		                              host='127.0.0.1',
		                              database='secure_banking_system')
		self.cursor = self.cnx.cursor()
		#self.cursor.execute('INSERT INTO conf(ID, conf_name) VALUES(8 , \'classified\');')
		#self.cnx.commit()


	def insert_into_table(self, username, password_hash, salt, confidentiality_level, integrity_level, number_of_attempts, block_time, is_block):
		self.cursor.execute('INSERT INTO users(username, password_hash, salt, confidentiality_level, integrity_level, number_of_attempts, block_time, is_block) VALUES(\'%s\',\'%s\',\'%s\',1,1,0,NULL,0);' %(username, password_hash, salt))
		self.cnx.commit()

	def close_connection(self):
		self.cursor.close()
		self.cnx.close()
