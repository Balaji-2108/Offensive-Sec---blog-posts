# DVR4 - Security Learning Summary (PG Practice)

## Introduction
This post documents security lessons learned from analyzing a Windows-based lab environment. The focus is on how insecure file handling and weak credential practices can be chained together to achieve full system compromise.
For this demonstration I used DVR4 machine from PG practice which rated as Hard by the community.

## Enumeration

Nmap scan results:
```
22/tcp open ssh Bitvise WinSSHD 8.48
135/tcp open msrpc Microsoft Windows RPC
139/tcp open netbios-ssn Microsoft Windows netbios-ssn
445/tcp open microsoft-ds?
8080/tcp open http-proxy
```
Initial enumeration revealed multiple exposed network services, including file sharing services and a web-based surveillance application. The web service became the primary attack surface due to its exposed functionality and public-facing nature.

![webpage](/writeups/Screenshots/DRV4/Argusweb.png)

The Argus website has two users in its user page.
```
1. Administrator
2. Viewer
```

Upon Public vulnerability research, I discovered that the Argus Surveillance DVR has Directory traversal Vulnerability. These weaknesses could allow unauthorized access to sensitive configuration and credential-related files.

[Argus Surveillance DVR 4.0.0.0 - Directory Traversal](https://medium.com/r/?url=https%3A%2F%2Fwww.exploit-db.com%2Fexploits%2F45296)

![exploit](/writeups/Screenshots/DRV4/exploitpage.png)

## Initial Foothold

Reviewing all the informations, we can try obtaining the ssh from the Users found in the Argus website.

The identified file access vulnerability allowed retrieval of sensitive authentication material associated with a low-privileged user account. This information was sufficient to gain an initial foothold on the system.

![curl](/writeups/Screenshots/DRV4/curl.png)

Using the private key I connected to the device via ssh connection.

![ssh](/writeups/Screenshots/DRV4/ssh.png)

_The Argus surveillance service has a Directory traversal Vulnerability which is then used to retrieve the SSH Private key of the user viewer, gaining a ssh shell to the machine._

## Escalation Privilege

Post-exploitation enumeration identified that the Argus Surveillance configuration files contains sensitive information and found that it stores the encrypted passwords in the DVRParams.ini, which can be encrypted using the below exploit.

[Argus Surveillance DVR 4.0 - Weak Password Encryption](https://medium.com/r/?url=https%3A%2F%2Fwww.exploit-db.com%2Fexploits%2F50130)

![DVR1](/writeups/Screenshots/DRV4/DVRparams.png)
![DVR1](/writeups/Screenshots/DRV4/DVRparams1.png)

Using the exploit, I decrypted the Password for the user "Administrator". To try this password, I first created a .exe file and uploaded it to the machine. Then I ran the exe file as the user administrator providing me the admin shell access.

![msfvenom](/writeups/Screenshots/DRV4/msfvenom.png)

![met](/writeups/Screenshots/DRV4/met.png)

![nc](/writeups/Screenshots/DRV4/nc.png)

## Summary

1. Identified a vulnerable surveillance application exposed via a web interface
2. Abused improper file access controls to obtain sensitive authentication data
3. Leveraged weak credential storage and password reuse for privilege escalation
4. Achieved full administrative access due to compounded misconfigurations
   
## Mitigation

1. Replace unsupported or unmaintained surveillance software with actively maintained alternatives
2. Enforce strict file access controls to prevent unauthorized file retrieval
3. Avoid credential reuse across services
4. Regularly audit exposed services and configurations


