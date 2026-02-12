# PG practice Zipper — Security Lessons

## Introduction

This Post documents my learnings while practicing an PG practice box called zipper. The focus is on understanding Local file Inclusion vulnerability (LFI) exploited via php wrappers in this scenario.

## Enumeration

Nmap scan results:

```
22/tcp open ssh OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open http Apache httpd 2.4.41 ((Ubuntu))
The scan revealed two open ports i.e, port 22 for ssh and port 80 for web service.
```
Port 80 hosts a web application called Zipper which converts any file into a compressed zip format.

![main page](/writeups/Screenshots/zipper/Zipper(main).png)
 
I tried uploading a php reverse file simple-backdoor.php and the website compressed it and returned a link to download the compressed zip file. This means the uploaded file is stored as zip file in the web page.

Next, I clicked on the home button and it redirected to the same page but with a different link appending “index.php?file=home”.

As the index.php gets a parameter called “file”, I tried php://filter wrappers in that parameter to check if we can handle the files in the web directory. Used the wrapper to extract index.php file in base64 format.

![exploit](/writeups/Screenshots/zipper/exploiting.png)
 
Webpage displaying index.php content in base64 format.

Now we can use this LFI to access the zip file which contains the reverse file. This can be done by zip:// wrapper.

_/index.php?file=zip://uploads/upload_1766650521.zip%23simple-backdoor_

Started a nc listener in my kali machine and accessed the file which gave me a shell access to the target.

![nclistner](/writeups/Screenshots/zipper/nclistner.png)
 
The uploaded PHP reverse shell was executed when included via the zip:// wrapper, resulting in remote code execution.
 
## Privilege Escalation

Enumerating inside the machine, I found a cron job which zips zip file in /var/www/html/uploads in to one and stores the logs of the operation as backup.log. The Operation is executed as root and according to the file the password for this operation is stored in /root/secret.

![Privesc](/writeups/Screenshots/zipper/Privesc.png)
 
Upon checking the uploads directory the enox.zip in symlinked to /root/secret.

_enox.zip → /root/secret_

As the cron job backups every file in uploads directory it should access the symlinked file which will throw the root credentials as a error in backup.log file, using it gave us the access to root shell of the machine.

Root privileges were successfully obtained due to cronjob misconfiguration, which leaked the root password from a sensitive file.

## Mitigation:

1.	Validate and sanitize the user input and harden the php configuration.
2.	Never allow user input without proper checks for file handling function.
3.	Check and eliminate any sensitive files that the cronjob is accessing that could leak sensitive information's.
   
## Summary:

The Zipper machine was compromised by exploiting a Local File Inclusion vulnerability in the file parameter. PHP stream wrappers such as php://filter were used to disclose application source code, and the zip:// wrapper enabled execution of a previously uploaded PHP reverse shell.
Privilege escalation was achieved by a misconfigured root cronjob. A symbolic link to /root/secret caused sensitive data to be written into a log file, ultimately revealing the root credentials.
