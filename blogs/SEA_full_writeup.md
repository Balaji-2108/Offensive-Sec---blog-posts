# SEA - Security Lesson

## Introduction:

Sea is a Proving Grounds (PG) Practice box that focuses on privilege escalation techniques. This post explains the techniques used to compromise the target system. The box is rated as Intermediate by the community.

## Enumeration:

Nmap scan results:
```
21/tcp open ftp vsftpd 3.0.5
 | ftp-anon: Anonymous FTP login allowed (FTP code 230)
 |_End of status
 22/tcp open ssh OpenSSH 9.6p1 Ubuntu 3ubuntu13.5 (Ubuntu Linux; protocol 2.0)
 80/tcp open http Apache httpd 2.4.58 ((Ubuntu))
 |http-title: Villa Agency - Real Estate HTML5 Template
 |_http-server-header: Apache/2.4.58 (Ubuntu)
 55743/tcp open http Apache httpd 2.4.58 ((Ubuntu))
 |_http-title: Sea
 | http-cookie-flags
 ```

## Initial Foothold:

As the box mainly focuses on privilege escalation, the initial foothold is intentionally made easier.

Port 21 (FTP):
1. Anonymous login is allowed.
2. It contains log files that reveal a PHP file location of interest.

![FTP](/writeups/Screenshots/SEA/FTP.png)
![logFTP](/writeups/Screenshots/SEA/logftp.png)

Accessing the identified location on the web application running on port 55743 reveals sensitive SSH credentials.

![webcred](/writeups/Screenshots/SEA/webcreds.png)

These credentials are then used to log in via SSH, providing the initial foothold.

![ssh](/writeups/Screenshots/SEA/ssh.png)

## Privilege Escalation:

Initial enumeration shows that the user nicolas can run a binary named ps with sudo permissions.

![sudol](/writeups/Screenshots/SEA/sudol.png)

However, no direct attack vector was found for this binary initially, so further enumeration was performed.
Using the tool pspy64, a cron job was identified running a bash script named bin_replacer with UID 0 (root).

![pspy](/writeups/Screenshots/SEA/pspy.png)

Upon reviewing the script:

1. It searches for any file in /home/nicolas/bin that contains a dot (.) in its name.
2. It then replaces the corresponding file in the /bin directory.

![binreplace](/writeups/Screenshots/SEA/binreplace.png)

This behavior can be abused by:

1. Creating a malicious script named .ps in the user's directory
2. Allowing the cron job to replace the legitimate ps binary in /bin

![script](/writeups/Screenshots/SEA/scriptsh.png)

Once the replacement occurs:

1. Since the user can run ps with sudo privileges,
2. The modified binary executes with root permissions, leading to privilege escalation.

![psbin](/writeups/Screenshots/SEA/psbin.png)
![root](/writeups/Screenshots/SEA/root.png)

Summary:

1. Anonymous FTP access exposed log files containing sensitive information
2. The log file revealed a hidden web resource
3. The web resource exposed SSH credentials, providing initial access
4. A misconfigured cron job allowed file replacement in system directories
5. Root access was achieved by abusing a sudo-allowed binary

Mitigation:

1. Disable anonymous FTP access unless absolutely necessary
2. Restrict access to log files and sensitive system information
3. Avoid exposing credentials through web applications
4. Do not use cron jobs that write or replace files in critical system directories
5. Grant NOPASSWD sudo access only when strictly required and limit it to safe binaries
