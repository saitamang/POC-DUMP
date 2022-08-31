# CVE-2022-37140
```
# Exploit Title: PayMoney 3.3 is vulnerable to Client Side Remote Code Execution (RCE).
# Date: 24/07/2022
# Exploit Author: saitamang
# Vendor Homepage: https://paymoney.techvill.org/
# Software Link: https://paymoney.techvill.org/
# Version: 3.3
```
## Description
The paymoney.techvill.org system suffers from Client Side Remote Code Execution (RCE) from uploading malicious RTF file. The vulnerability exist on reply ticket function and upload the malicious file. A calculator will open when the victim who download the file open the RTF file.

## Attack Vector
1. The attacker create the malicious macro file
<img src="https://github.com/saitamang/POC-DUMP/blob/main/PayMoney/img/rce/1-create%20macro.png?raw=true">

2. The file is then uploaded
<img src="https://github.com/saitamang/POC-DUMP/blob/main/PayMoney/img/rce/2-upload%20malicous%20rtf.png?raw=true">

3. If the user download the file, the file can be executed and gain the client side RCE.
<img src="https://github.com/saitamang/POC-DUMP/blob/main/PayMoney/img/rce/3-click%20and%20file%20downloaded.png?raw=true">

4. The RCE executed on client side.
<img src="https://github.com/saitamang/POC-DUMP/blob/main/PayMoney/img/rce/4-calculator%20pop%20up.png?raw=true">

# CVE-2022-37137
```
# Exploit Title: PayMoney 3.3 is vulnerable to Stored Cross-Site Scripting (XSS) during replying the ticket
# Date: 24/07/2022
# Exploit Author: saitamang
# Vendor Homepage: https://paymoney.techvill.org/
# Software Link: https://paymoney.techvill.org/
# Version: 3.3
```

## Description
The XSS can be obtain from injecting under "Message" field with "description" parameter with the specially crafted payload to gain Stored XSS.
The XSS then will prompt after that or can be access from the view ticket function.

## Attack Vector
1. The user first must created a ticket.
<img src="https://raw.githubusercontent.com/saitamang/POC-DUMP/main/PayMoney/img/xss1/1.png">

2. Then on the replying the ticket under "Message" field with "description" parameter, inject the payload below to gain Stored Cross-Site Scripting(XSS).
```
"><svg/onload=alert(document.cookie)>
```
<img src="https://github.com/saitamang/POC-DUMP/blob/main/PayMoney/img/xss1/2.png?raw=true">

<img src="https://github.com/saitamang/POC-DUMP/blob/main/PayMoney/img/xss1/3.png?raw=true">

3. The XSS will prompt or can be access from the view ticket function

<img src="https://github.com/saitamang/POC-DUMP/blob/main/PayMoney/img/xss1/4.png?raw=true">


