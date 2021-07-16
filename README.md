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
* from Crypto.Util.Padding import pad, unpad -> ``pip3 install pycryptodome``
* ``pip3 install pycryptodome``
* ``pip3 install scrypt``
* ``pip3 install registry``

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
* Changing the state of the system after a user logs in for more security.
* Implementing Salting [link](https://www.geeksforgeeks.org/implementing-salting/)

## [Cryptography:](https://github.com/arman324/Secure-Banking-System/blob/main/Cryptography.py)
### Cryptography class features:
* Symmetric cryptography
>* Session key -> It will be expired after 5 minutes.
* Asymmetric cryptography

## [Access Control:](https://github.com/arman324/Secure-Banking-System/blob/main/AccessControl.py)
### AccessControl class features:
* DAC
* MAC
>* BLP
>* BIBA

## [Banking Operationl:](https://github.com/arman324/Secure-Banking-System/blob/main/BankingOperation.py)
### BankingOperation class features:
* Create [account_type] [amount] [conf_label] [integrity_label]
* Join [account_no]
* Accept [username] [conf_label] [integrity_label]
* Show_MyAccount
* Show_Account [account_no]
* Deposit  [to_account_no] [amount]
* Withdraw [from_account_no] [to_account_no] [amount]

## [HoneyPot:](https://github.com/arman324/Secure-Banking-System/blob/main/BankingOperationHoneyPot.py)
### BankingOperationHoneyPot class features:
* Generally, a honeypot consists of data that appears to be a legitimate part of the site and contains information or resources of value to attackers. It is actually isolated, monitored, and capable of blocking or analyzing the attackers. [link](https://en.wikipedia.org/wiki/Honeypot_(computing)) 
* In this project, the attacker will access fake banking operations after entering the wrong passwords 6 times.
* Everything is logged in this section to identify the attacker's motive.

## [logging:](https://github.com/arman324/Secure-Banking-System/blob/6acfcfe8c522cd957e8d13a66779544db80c978c/MysqlConnection.py#L375)
* The purpose of logging is to track error reporting and related data in a centralized way.

<img width="800" alt="Screen Shot 2021-07-16 at 10 47 23 PM" src="https://user-images.githubusercontent.com/35253872/125991697-fdaad7f7-d44a-452d-aabd-49fe0daaa3de.png">



## Support
Reach out to us at:
* riasiarman@yahoo.com
* elitoulabin@gmail.com
* ghazalze@yahoo.com
