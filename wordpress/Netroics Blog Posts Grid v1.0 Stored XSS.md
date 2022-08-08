```
# Exploit Title: Stored XSS in post_title parameter in WordPress Plugin "Netroics Blog Posts Grid" v1.0
# Date: 08/08/2022
# Exploit Author: saitamang , syad , yunaranyancat
# Vendor Homepage: wordpress.org
# Software Link: https://downloads.wordpress.org/plugin/netroics-blog-posts-grid.zip
# Version: 1.0
# Tested on: Centos 7 apache2 + MySQL

WordPress Plugin "Netroics Blog Posts Grid" is prone to a stored cross-site scripting (XSS) vulnerability because it fails to properly sanitize user-supplied input. An attacker may leverage this issue to execute arbitrary script code in the browser of an unsuspecting user in the context of the affected site. This can allow the attacker to steal cookie-based authentication credentials and launch other attacks. WordPress Plugin "Netroics Blog Posts Grid" version 1.0 is vulnerable; prior versions may also be affected.

Login as Editor > Add testimonial > Under Title inject payload below ; parameter (post_title parameter) > Save Draft > Preview the post


payload --> user s1"><img src=x onerror=alert(document.cookie)>.gif


The draft post can be viewed using other Editor or Admin account and Stored XSS will be triggered.

Further information can be preview from github below:
https://github.com/saitamang/POC-DUMP/blob/main/wordpress/Netroics%20Blog%20Posts%20Grid%20v1.0%20Stored%20XSS.md

```
# Step to Reproduce
1 - Login as an Editor and create a new Netroics Post from the Plugin. Insert payload as mentioned above and saved as Draft.
<img src=https://github.com/saitamang/POC-DUMP/blob/main/wordpress/img/1-editor%20create%20post%20save%20as%20draft.png>

2- Login as other Editor or Admin can preview the Draft Post
<img src=https://github.com/saitamang/POC-DUMP/blob/main/wordpress/img/2-other%20users%20including%20admin%20can%20view%20draft.png>

3- Click the link for preview
<img scr=https://github.com/saitamang/POC-DUMP/blob/main/wordpress/img/3-click%20the%20link%20or%20preview.png>

4- XSS will prompt
<img src=https://github.com/saitamang/POC-DUMP/blob/main/wordpress/img/4-xss%20prompt%20when%20open%20link.png>
