# Secure-Banking-System :)
## Overview
### Common security mechanisms that have been implemented in this project are:
1. Cryptography 
2. Access Control
3. Authentication
4. Audit

## Requirements
* [MySQL](https://www.mysql.com) -> ``sudo apt-get install mysql-server``
* Python 3.x
* import cryptography  -> ``pip3 install cryptography``
* import mysql.connector -> ``python3 -m pip install mysql-connector``

## How to Run
First of all:
1. ``mysql -u your_username -p your_password``
2. ``use db_name``
3. ``source <path_to_sql_file>/secure_banking_system.sql``

Then:
1. ``Python3 Server.py``
2. ``Python3 Client.py``

## [Signup:](https://github.com/arman324/Secure-Banking-System/blob/main/Signup.py)
### Signup class features:
* Checking the strength of the input password for ```Authentication```
* Adding Salt and hash the input password for ```Authentication```

## [Login:](https://github.com/arman324/Secure-Banking-System/blob/main/Login.py)
### Login class features:
* Backoff mechanism for ```Authentication```

## Support
Reach out to us at:
* riasiarman@yahoo.com
* [@ellietoulabi](https://github.com/ellietoulabi)
* ghazalze@yahoo.com
