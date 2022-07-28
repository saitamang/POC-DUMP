# Loan Management System

Loan Management System suffers from severals vulnerabilities which is SQL Injection and Stored Cross Site Scripting (XSS).

## 1. SQL Injection

The attack vector for the SQL Injection happened at the login page. The login can be bypass using the boolean payload below to gain access as Admin as the highest privileges.

`Payload --> 'or 2=2#`

The python script to get the database name from SQL Injection Vulnerability can be access [here](https://github.com/saitamang/POC-DUMP/blob/main/Loan%20Management%20System/sqli-getdb.py).

<--!<img src="https://raw.githubusercontent.com/saitamang/POC-DUMP/main/Loan%20Management%20System/img/script.png" title="hack">-->

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
