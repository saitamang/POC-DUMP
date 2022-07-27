# Loan Management System

Loan Management System suffers from severals vulnerabilities which is SQL Injection and Stored Cross Site Scripting (XSS).

## 1. SQL Injeection

The attack vector for the SQL Injection happened at the login page. The login can be bypass using the boolean payload below to gain access as Admin as the highest privileges.

`Payload --> 'or 2=2#`

## 2. Stored Cross Site Scripting

There are several functions and parameter affected as below:

<pre><code>addUser.php
- firstname
- lastname

save_ltype.php
- ltype_name
- ltype_desc

save_borrower.php
- firstname
- middlename
- lastname
- address
</code></pre>

The payload use to inject is `"/><svg/onload=alert(document.cookie)>`

p/s : The python script will be release soon to get the database name fro SQL Injection Vulnerability
