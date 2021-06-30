# CVE-2021-35960
Writeup for Stored Cross-Site Scripting(XSS) and HTML Injection at "sectionName" on SAS® Web Report Studio 4.4

### :computer: Stored Cross-Site Scripting(XSS) on SAS® Web Report Studio 4.4 :computer:

\[1.\] Login to your system > Click "New Report"
<br>
<img src="https://github.com/saitamang/POC-DUMP/blob/main/SAS/Web%20Report%20Studio/img/1-%20create%20report.png" title="1">
<br><br>
[2.] Under "Table of Contents" on the left side, click the drop down and choose "Insert a New Section ..."
<br>
<img src="https://github.com/saitamang/POC-DUMP/blob/main/SAS/Web%20Report%20Studio/img/2-%20insert%20new%20section.png" title="2">
<br><br>
[3.] New Window will pop-up to create a new section, Open your proxy and turn intercept "ON"
<br>
<img src="https://github.com/saitamang/POC-DUMP/blob/main/SAS/Web%20Report%20Studio/img/3-%20intercept%20proxy.png" title="3">
<br><br>
[4.] Click "OK" button > under "sectionName" parameter, insert payload(below) 
<br><br>
**payload** : `"></option></select><marquee/onstart=confirm(1337)>`
<br><br>
<img src="https://github.com/saitamang/POC-DUMP/blob/main/SAS/Web%20Report%20Studio/img/3%20-%20insert%20payload%20xss.png" title="4">
<br><br>
[5.] Click "Forward" to forward the request and turn the intercept OFF > XSS will prompt
<br>
<img src="https://github.com/saitamang/POC-DUMP/blob/main/SAS/Web%20Report%20Studio/img/4-%20xss%20prompt.png" title="5">
<br><br>


Cheers! :)
