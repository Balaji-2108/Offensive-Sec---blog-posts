# PG practice Zipper — Security Lessons

## Platform
Proving Grounds Practice

## Difficulty
Hard

## Objective
Practice identifying and exploiting common web application misconfigurations and Linux privilege escalation issues in an OSCP-style lab environment.

---

## High-Level Attack Path
- Identified multiple exposed services during initial enumeration
- Discovered a service called zipper running on a standard HTTP port
- Zipper service converts any file into a compressed zip format
- Insecure file handling functionality and unsanitizied user input enabled remote code execution
- Misconfigured cron job linked to a sensitive file allowed privilege escalation to root

---

## Enumeration Techniques Used
- TCP service discovery and version identification
- Web service enumeration on standard
- Manual inspection of Zipper web service
- Local file Inclusion vulnerability test
- Manual php wrappers test

---

## Vulnerability Categories Identified
- Improper file Handling functionality
- Lack of user input sanitization
- Misconfigured root cronjob
- Cronjob leaking Sensitive file information

---

## Tools Used
- Network scanning tools
- Web enumeration tools
- PHP wrappers research
- Local privilege escalation enumeration utilities

---

## Key Takeaways
- Check for LFI in a file upload based web services
- File upload functionality should always be treated as high risk
- Purpose built cronjob may have sensitive infomation directly if not indirectly

---

## Defensive Mitigations
- Validate and sanitize the user input and harden the php configuration.
- Apply strict validation and sandboxing for uploaded files
- Check and eliminate any sensitive files that the cronjob is accessing

---

## Disclaimer
This writeup is based on a controlled lab environment and focuses on high-level security learning outcomes. No exploit code, credentials, or step-by-step attack instructions are included.
