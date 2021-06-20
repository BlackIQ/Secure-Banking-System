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
		#self.cursor.execute('INSERT INTO conf(ID, conf_name) values(8 , \'classified\');')
		#self.cnx.commit()

	def close_connection(self):
		self.cursor.close()
		self.cnx.close()
