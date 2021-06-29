# CVE-2021-#####
Writeup for Stored Cross-Site Scripting(XSS) on SAS® Web Report Studio 4.4

### :computer: XSS on SAS® Web Report Studio 4.4 :computer:

\[1.\] Login to your system > On "Resource" tab > "Browse"
<br>
<img src="https://raw.githubusercontent.com/saitamang/CVE-2021-35475/main/img/1-Browse.png" title="1">
<br><br>
[2.] Choose a "Platform"
<br>
<img src="https://raw.githubusercontent.com/saitamang/CVE-2021-35475/main/img/2-Choose%20platform.png" title="2">
<br><br>
[3.] Click "Inventory" tab > Under "Servers" tab click "New..."
<br>
<img src="https://raw.githubusercontent.com/saitamang/CVE-2021-35475/main/img/3-inventory-new-server.png" title="3">
<br><br>
[4.] Under "General Properties" tab on "Name" field , put the payload(below) > Filled up other information and click "Ok" button 
<br><br>
**payload** : XSS"><marquee onstart=confirm('XSS')>@SAITAMANG
<br><br>
<img src="https://raw.githubusercontent.com/saitamang/CVE-2021-35475/main/img/4-add%20new%20server%20with%20xss%20payload.png" title="4">
<br><br>
[5.] Successfully saved the payload
<br>
<img src="https://raw.githubusercontent.com/saitamang/CVE-2021-35475/main/img/5-xss%20successfully%20saved.png" title="5">
<br><br>
[6.] Then scroll down to bottom under "Configuration Properties" tab > click "Edit" button
<br>
<img src="https://raw.githubusercontent.com/saitamang/CVE-2021-35475/main/img/6-scroll%20bottom%20press%20edit.png" title="6">
<br><br>
[7.] Then the payload will be executed
<br>
<img src="https://raw.githubusercontent.com/saitamang/CVE-2021-35475/main/img/7-xss%20prompt.png" title="7">
<br><br>

  
  Cheers! :)
