from MysqlConnection import MysqlConnection

class AccessControl:
    
    def __init__(self, MysqlConnection):
        self.MysqlConnection=MysqlConnection
        
    def sayHelloToAccessControl(self):
        return "One batch Two batch Penny and Dime"
        
    
    