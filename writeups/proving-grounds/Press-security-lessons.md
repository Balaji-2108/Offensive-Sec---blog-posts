# Press – Security Learning Summary

## Platform
Proving Grounds Practice

## Difficulty
Easy

## Objective
Practice identifying and exploiting common web application misconfigurations and Linux privilege escalation issues in an OSCP-style lab environment.

---

## High-Level Attack Path
- Identified multiple exposed services during initial enumeration
- Discovered a content management system running on a non-standard HTTP port
- Weak authentication allowed administrative access
- Insecure file handling functionality enabled remote code execution
- Misconfigured sudo permissions allowed privilege escalation to root

---

## Enumeration Techniques Used
- TCP service discovery and version identification
- Web service enumeration on both standard and non-standard ports
- Manual inspection of CMS functionality
- Basic authentication testing

---

## Vulnerability Categories Identified
- Weak / default credentials
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
- Non-standard ports often host high-value services
- Weak credentials remain one of the most common real-world issues
- File upload functionality should always be treated as high risk
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
