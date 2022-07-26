## Hospital Information System

Other refrence --> https://packetstormsecurity.com/files/167803/Hospital-Information-System-1.0-SQL-Injection.html

From the login page, at the email form, the attacker may fill anything inside. On the password form, the attacker may used below payload and click login to successfully login as Admin functionality.

Payload --> 'or 1=1#

## Login bypass using normal SQLI payload

<img src="https://github.com/saitamang/POC-DUMP/blob/main/Hospital%20Information%20System/img/login-success.png?raw=true" title="login">


## Login bypass with Sleep validation

<img src="https://github.com/saitamang/POC-DUMP/blob/main/Hospital%20Information%20System/img/proven-sleep.png?raw=true" title="sleep">


## Checking length of column

<img src="https://github.com/saitamang/POC-DUMP/blob/main/Hospital%20Information%20System/img/length-column.png?raw=true" title="length">

##You may download script automation to get the database name for your reference to learn!

Download [here](https://github.com/saitamang/POC-DUMP/blob/main/Hospital%20Information%20System/sqli.py)
