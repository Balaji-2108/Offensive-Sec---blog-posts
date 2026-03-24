# BitForge (PG Practice) — Security Lessons

## Introduction:

In this write-up, I explain how exposure of sensitive files on a web server can lead to a full system compromise.
For this demonstration, I used the BitForge machine from Proving Grounds Practice, which is rated Hard by the PG community.

### Enumeration:

Nmap scan Results

```
22/tcp open ssh OpenSSH 9.6p1 Ubuntu 3ubuntu13.5
80/tcp open http Apache httpd
3306/tcp open mysql MySQL 8.0.40–0ubuntu0.24.04.1
The scan revealed a web service running on port 80 and a MySQL service on port 3306.
```

**Port 80 Enumeration**

A website named bitforge was hosted in port 80.

While browsing the application, the “**EMPLOYEE PLANNING PORTAL**” tab redirects to SOplanning v1.52.01 login page.

![webpage](/writeups/Screenshots/bitforge/webapp.png)

A search revealed a known **authenticated RCE vulnerability** for this version of SOPlanning. However, valid credentials were required to exploit it.

[SOplanning v1.52.01 - RCE(Authenticated)_exploit_db](https://www.exploit-db.com/exploits/52082?source=post_page-----ce320cbf182b---------------------------------------)

Further enumeration using Gobuster revealed an exposed .git directory.

```
Note: The .git folder is the core of a Git repository, containing all the metadata, object database, and history for your project. It is essentially the entire Git repository for the local project, stored as a hidden directory to prevent accidental modification or deletion.
```

![webgit](/writeups/Screenshots/bitforge/webgit.png)

I mirrored the .git directory locally and analyzed it using Git commands:

git log — shows the project commit history

git show <commit> — Displays the commit message.

![wgetgit](/writeups/Screenshots/bitforge/wgetgit.png)

![gitlog](/writeups/Screenshots/bitforge/gitlog.png)

The commit hash from the above command is used to display the commit message and it revealed a database password for user **BitForgeAdmin**

![gitshow](/writeups/Screenshots/bitforge/gitshow.png)

Using the discovered credentials, I connected to the MySQL service on port 3306.

![mysql](/writeups/Screenshots/bitforge/mysql.png)

Database Enumeration:

The mysql service contains a password hash for the Soplanning admin in the bitforge_customer_db database.

![mysql1](/writeups/Screenshots/bitforge/mysql1.png)

I tired cracking the hash with different kind of tools, but none of them worked. During my research on cracking the password, I found a SOplanning github page.

[SO Planning github page](https://github.com/Worteks/soplanning?source=post_page-----ce320cbf182b---------------------------------------)

This page contains all information about the service and a file named **demo_data.inc (soplanning/blob/master/includes/demo_data.inc)** contains initial database credentials used while setting up the service.
```
Username: admin
Password: admin
```

I used the password hash from the file and replaced it in the bitforge_customer_db database.

![demodata](/writeups/Screenshots/bitforge/demodata.png)

![mysql2](/writeups/Screenshots/bitforge/mysql2.png)

Now that I have changed the admin password which is “admin”, I successfully exploited the **authenticated RCE vulnerability** in SOPlanning, gaining a shell on the system.

![52082](/writeups/Screenshots/bitforge/52082.png)

![nc](/writeups/Screenshots/bitforge/netcat.png)

## Privilege Escalation:

**Local Enumeration:**

Running **linPEAS** did not reveal an immediate privilege escalation vector but identified a user named jack.

Using **pspy64**, I monitored background processes and discovered an automated MySQL command running with credentials belonging to user jack.

Using these credentials, I logged in via SSH as jack.

![pspy64](/writeups/Screenshots/bitforge/pspy64.png)

I tried logging in via ssh and I got connected as user jack.

![ssh](/writeups/Screenshots/bitforge/ssh.png)

## Sudo Misconfiguration:

Further enumeration revealed that user jack had **NOPASSWD sudo privileges** for the following binary:

![sudol](/writeups/Screenshots/bitforge/sudol.png)

![fpasschange](/writeups/Screenshots/bitforge/fpasschange.png)

Upon inspecting the binary, I found that it is changing directory to /opt/password_change_app before excuting the flask command. Listing the content of the folder revealed a python file app.py. This file is a basic HTML webpage for the flask_password_changer.

![lsla](/writeups/Screenshots/bitforge/lsla.png)

The file has write access for the user jack. Modifying the app.py file with a malicious script and executing the flask as sudo will execute the script as root user. I added the below script to the app.py.

```
import os
os.system("chmod u+s /usr/bin/bash")
```

Now, executing the /usr/bin/flask_password_changer as sudo will give us the root access to the machine.

![bashp](/writeups/Screenshots/bitforge/bashp.png)

## Summary:

The exposed .git folder revealed a database password. The database contains the admin password for SOplanning. The admin password was unable to crack hence the password was changed in the database. With the credentials, Authenticated RCE exploit on SOplanning was used to gain a shell access.

Found a user named jack, who as a automation script mysql running with credentials. The credentials were retrieved with pspy64 tool and logged in via ssh as jack. User jack has NOPASSWD privilege for the command /usr/bin/flask_password_changer which was exploited as the low privilleged user has the write access.

## Mitigation:

1. Restrict the access to sensitive information via server configuration.
2. Regularly audit and update the website services.
3. Never hardcode the credentials in cronjob or the script files.
4. Use secure credential storage with restricted permissions
5. Avoid granting NOPASSWD sudo access to binaries that rely on writable files


