# Sauna HTB — Security lessons
## Introduction:

AS-REP roasting and AutoLogon credentials are still major security risks in Active Directory environments.
In this write-up, I document how these weaknesses can be exploited on a Domain Controller and how such risks can be mitigated.

For this demonstration, I used the Sauna Active Directory machine from HTB.

## Enumeration:

Nmap Scan results:

```
80/tcp open http Microsoft IIS httpd 10.088/tcp open kerberos-sec Microsoft Windows Kerberos (server time: 2025–12–30 16:43:30Z)
135/tcp open msrpc Microsoft Windows RPC
139/tcp open netbios-ssn Microsoft Windows netbios-ssn
389/tcp open ldap Microsoft Windows Active Directory LDAP (Domain: EGOTISTICAL-BANK.LOCAL0., Site: Default-First-Site-Name)
445/tcp open microsoft-ds?
464/tcp open kpasswd5?
593/tcp open ncacn_http Microsoft Windows RPC over HTTP 1.0
636/tcp open tcpwrapped
3268/tcp open ldap Microsoft Windows Active Directory LDAP (Domain: EGOTISTICAL-BANK.LOCAL0., Site: Default-First-Site-Name)
3269/tcp open tcpwrapped
5985/tcp open http Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
```

While enumerating SMB, RPC, and HTTP services, the About page on the web server revealed a list of employee names.

![webpage](/writeups/Screenshots/Sauna/webpage.png)

Using username-anarchy, I generated multiple username combinations from the discovered names.

These usernames were tested with Kerbrute, which revealed a valid domain user:

![kerbrute](/writeups/Screenshots/Sauna/kerbrute.png)

## AS_REP Roasting:

Since no credentials were available, I attempted AS-REP roasting using the valid username.

```
Note: AS-REP Roasting is a credential-dumping attack technique to extract and crack password hashes from user accounts in a Microsoft Active Directory (AD) environment that have a specific misconfiguration: Kerberos pre-authentication is disabled.
```

![AS-REP](/writeups/Screenshots/Sauna/AS-REP.png)

A Kerberos hash was successfully retrieved and cracked using Hashcat, revealing the password for **fsmith**.

## Post-Exploitation Enumeration

## WinPEAS:

Running **winPEAS** revealed that the user SVC_LOANMGR has autologon enabled and the autologon credentials.

![winpeas](/writeups/Screenshots/Sauna/winPEAS.png)

Now, we have credentials for users fsmith and svc_loamgr. With these I tried enumerating RPC and smbclient again, but no interesting things found in them.

## BloodHound:

Using **SharpHound**, I collected Active Directory data and analyzed it in **BloodHound**. The path finder option revealed that the svc_loanmgr has a interesting privilege over the dc controller know as DCsync.

![bloodhound](/writeups/Screenshots/Sauna/bloodhound.png)

## DCsync Attack:

A search on dcsync attacks revealed that this privilege can be exploited using secretsdump.py to dump the password hashes from the Domain Controller

Using **secretsdump.py**, I performed a DCSync attack and successfully dumped the **Administrator NTLM hash** from the domain controller.

![secretsdump](/writeups/Screenshots/Sauna/secretsdumps.png)

By passing the hash, I obtained **Domain Administrator** access, fully compromising the domain.

## Summary:

By retrieving a valid User’s (fsmith) password hash by AS-REP roasting. The further enumeration using the found credential revealed a autologon credential of the user svc_loanmgr.

The Bloodhound path finder option revealed that the svc_loanmgr has DCsync function on the Domain controller. The DCsync function was exploited using secretsdump.py to retrieve the Administrator hash which gives us most the privileged access to the DC.

## Mitigation:

1. Enable the Kerberos pre-authentication for all users
2. Enforce strong password policies
3. The autologon function must be disabled for the users with high privilege.
4. Restrict replication (DCSync) permissions to only necessary accounts
5. Regularly audit AD permissions and service accounts
