# CVE-2022-3231

# Description

Stored Cross-Site Scripting (XSS) vulnerability in LibreNMS v22.8.0 allows attackers to execute arbitrary javascript code in the browser affected from function of "Schedule Maintenance" in "Title" parameter.
Proof of Concept

1 - Click "Alerts" > Click "Schedule Maintenance" from the dropdown

2 - Create a new schedule by clicking "Schedule Maintenance" green button

3 - Under "Title" , use payload below
```
saitamang"><iMg SrC="x" oNeRRor="alert(document.cookie);">
```
4 - Saved the new schedule by clicking the green button name "Schedule Maintenance"

5 - XSS will prompt afterwards.

# PoC Image


# PoC Video
```
https://drive.google.com/file/d/1sWsIJsENvwhig5notCKWh2C6_h-MvBN0/view?usp=sharing
```

# Impact

This vulnerability allows attackers to hijack the user's current session, steal relevant information, deface website or direct users to malicious websites and allows attacker to use for further exploitation.
