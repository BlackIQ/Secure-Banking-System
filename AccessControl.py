from MysqlConnection import MysqlConnection

class AccessControl:
    
    def __init__(self, MysqlConnection):
        self.MysqlConnection=MysqlConnection
        
    def sayHelloToAccessControl(self):
        return "One batch Two batch Penny and Dime"
    
    def has_write_access(self, username, account_no):
        response, user_integrity_label,user_confidentiality_label,acc_integrity_label,acc_confidentiality_label = self.MysqlConnection.get_security_labels(username, account_no)
        # print (response, " user Int:",user_integrity_label," usr cong:",user_confidentiality_label," acc int:",acc_integrity_label," acc conf:",acc_confidentiality_label)
        if user_integrity_label == -1 and user_confidentiality_label== -1 and acc_integrity_label== -1 and acc_confidentiality_label == -1:
            return 0,response
        else:
            if user_integrity_label >= acc_integrity_label and user_confidentiality_label <= acc_confidentiality_label:
                return 1, response
            else:
                return 0, "Write Access Denied."
    
    def has_read_access(self, username, account_no):
        
        response, user_integrity_label,user_confidentiality_label,acc_integrity_label,acc_confidentiality_label = self.MysqlConnection.get_security_labels(username, account_no)
        # print (response, " user Int:",user_integrity_label," usr cong:",user_confidentiality_label," acc int:",acc_integrity_label," acc conf:",acc_confidentiality_label)
        if user_integrity_label == -1 and user_confidentiality_label== -1 and acc_integrity_label== -1 and acc_confidentiality_label == -1:
            return 0,response
        else:
            if user_integrity_label <= acc_integrity_label and user_confidentiality_label >= acc_confidentiality_label:
                return 1, response
            else:
                return 0, "Read Access Denied."

        
    
    