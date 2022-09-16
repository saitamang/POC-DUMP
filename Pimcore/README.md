# CVE-2022-3211

```
# Exploit Title: Stored Cross Site Scripting (XSS) via "properties" during creating new users in pimcore/pimcore
# Exploit Author: saitamang
# Vendor Homepage: https://pimcore.com/en
# Software Link: https://github.com/pimcore/pimcore
# Version: 10.5.5
```

# PoC
login > click people icon at the left bar > click "Customers" > Click "New Customer" button from page > Fill up the "Edit" tab > Click "Save" button above > Click "Properties" tab > From "Add a custom Property" field , add "Test" on the first field > Click and select "text" on the second field > Click "+" button at the right of the field > On the table, click the key field to edit and add payload below:
```
mang"><img/src=x onerror=alert(/xss/)>
```
Then the XSS will triggered once the click any place in page.

# Video PoC
```
https://drive.google.com/file/d/1sfuiGp_c0AqBth55aR5tEdmVNka_BG0x/view?usp=sharing
```

# Image PoC

<img src="https://lh3.googleusercontent.com/drive-viewer/AJc5JmRVrISc9-r8v7PBLiduVGQo-jPUrGvWQIUeOLG3vM8Vxz3IHRpoXi645b6Y0ZSBiMSpG8-Dch8=w1920-h937" title="pimcore">

# Line of fixes
• <a href="https://github.com/pimcore/pimcore/commit/0508c491c6a4f3d119ec8dcf444e52ff25028c36">Here</a>

The report also can be seen <a href="https://huntr.dev/bounties/31ac0506-ae38-4128-a46d-71d5d079f8b7/">here</a>.
