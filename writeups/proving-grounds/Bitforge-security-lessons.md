# BitForge – Security Learning Summary

## Platform
Proving Grounds Practice

## Difficulty
 Medium

## Objective
Practice identifying and exploiting exposed sensitive files on webserver, in an OSCP-style lab environment.

---

## High-Level Attack Path
- Identified multiple exposed services during initial enumeration
- Discovered a project management system running on a standard HTTP port
- Exposed git folder revealing sensitive information leading to compromise the webservice
- Authenticated users has Insecure file handling functionality enabled remote code execution
- Hardcoded password in automation task, used to move laterally in the machine
- Misconfigured sudo permissions allowed privilege escalation to root

---

## Enumeration Techniques Used
- TCP service discovery and version identification
- Web service enumeration on both standard and non-standard ports
- Manual inspection of CMS functionality
- Basic authentication testing

---

## Vulnerability Categories Identified
- Exposed sensitive directories
- Outdated third-party CMS
- Insecure file upload handling
- Improper sudo privilege configuration

---

## Tools Used
- Network scanning tools
- Web enumeration tools
- CMS vulnerability research
- Local privilege escalation enumeration utilities

---

## Key Takeaways
- Exposure of sensitive files can lead to entire system compromise 
- File upload functionality should always be treated as high risk
- Never hardcode the credentials in cronjob or the script files
- Sudo permissions should be reviewed early during Linux privilege escalation

---

## Defensive Mitigations
- Enforce strong and unique passwords for administrative interfaces
- Keep CMS software up to date with security patches
- Apply strict validation and sandboxing for uploaded files
- Avoid passwordless sudo access for system binaries
- Follow the principle of least privilege for all users

---

## Notes for OSCP Preparation
- This machine reinforces the importance of thorough web enumeration
- CMS version disclosure can significantly reduce attack complexity
- Simple misconfigurations can be chained into full system compromise

---

## Disclaimer
This writeup is based on a controlled lab environment and focuses on high-level security learning outcomes. No exploit code, credentials, or step-by-step attack instructions are included.

- 🔗 Detailed Demonstration - [Press PG Practice — Full writeup](/blogs/Bitforge_full_writeup.md)
