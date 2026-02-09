# Sauna – Security Learning Summary

## Platform
Proving Grounds Practice

## Difficulty
 Medium

## Objective
Practice identifying and exploiting common Active Directory misconfigurations, including weak Kerberos configurations and improper access control, in an OSCP-style lab environment.

---

## High-Level Attack Path
- Identified the target as an Active Directory environment through service enumeration
- Collected publicly exposed information to derive potential domain usernames
- Discovered a domain account with Kerberos pre-authentication disabled
- Recovered credentials through offline password cracking
- Authenticated to the domain as a low-privileged service account
- Abused improper Active Directory permissions to escalate privileges
- Achieved full domain compromise

---

## Enumeration Techniques Used
- TCP service discovery and Active Directory service identification
- Web-based information gathering for user enumeration
- Kerberos enumeration for misconfigured domain accounts
- Active Directory object and permission analysis

---

## Vulnerability Categories Identified
- Kerberos pre-authentication disabled (AS-REP roasting)
- Weak password hygiene on service accounts
- Excessive or misconfigured Active Directory permissions
- Inadequate monitoring of privileged directory operations

---

## Tools Used
- Network scanning tools
- Kerberos enumeration utilities
- Offline password cracking tools
- Active Directory analysis and visualization tools

---

## Key Takeaways

- Public-facing information can significantly aid domain user enumeration
- Kerberos misconfigurations can lead to credential compromise without authentication
- Service accounts are frequent targets due to weak password practices
- Active Directory permission abuse can result in complete domain takeover
- Understanding attack paths is more important than individual exploits

---

## Defensive Mitigations
- Enforce Kerberos pre-authentication for all domain accounts
- Apply strong, unique passwords for service accounts
- Regularly audit Active Directory access control lists (ACLs)
- Restrict high-impact permissions such as replication rights
- Monitor and alert on suspicious Kerberos and directory activities

---

## Notes for OSCP Preparation
- Reinforces the importance of recognizing Active Directory attack surfaces early
- Highlights Kerberos-related attacks commonly seen in OSCP exams
- Demonstrates how multiple low-severity issues can be chained into domain compromise
- Emphasizes structured enumeration over tool dependency

---

#Disclaimer
This writeup is based on a controlled lab environment and focuses on high-level security learning outcomes.
No exploit code, credentials, or step-by-step attack instructions are included.


- 🔗 Detailed explanation can be found in this blog - [Sauna HTB — Security lessons](https://medium.com/@balajibala2118/sauna-htb-security-lessons-315b1cfb656d)
