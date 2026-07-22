# 🛡️ HTTP Security Analyzer

A Python-based web security assessment tool that analyzes HTTP response headers, cookie security, and server information to identify common web security misconfigurations. The tool generates a professional HTML report to help security professionals quickly assess the security posture of web applications.

---

## ✨ Features

- 🔍 Analyze HTTP response security headers
- 🍪 Inspect cookie security attributes
- 🖥️ Detect server banner disclosure
- 📊 Calculate an overall security score and grade
- 📄 Generate a professional HTML report
- 💻 Easy-to-use Command Line Interface (CLI)

---

## 🔎 Security Checks

### HTTP Security Headers

The analyzer checks for the presence of:

- Content-Security-Policy (CSP)
- Strict-Transport-Security (HSTS)
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy

### Cookie Security

The analyzer verifies whether cookies have:

- Secure
- HttpOnly
- SameSite

### Information Disclosure

Checks for:

- Server banner disclosure
- Missing security headers
- Insecure cookie attributes

---

## 📂 Project Structure

```
HTTP-Security-Analyzer/
│
├── analyzer.py           # Main application
├── checks.py             # Security checks
├── report.py             # HTML report generation
├── templates/
│   └── report.html       # Jinja2 HTML template
├── output/
│   └── sample.html
├── requirements.txt
└── README.md
```

---

## 🛠 Requirements

- Python 3.10+
- requests
- colorama
- jinja2

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Analyze a website:

```bash
python analyzer.py -u https://example.com
```

---

## ⚙️ Command Line Options

| Option | Description |
|---------|-------------|
| `-u` | Target URL |
| `-h` | Show Help |
| `--file` | Filename (Default - report.html) |

Example:

```bash
python analyzer.py -u https://example.com
```

---

## 📊 Sample Output

```
================================================

HTTP Security Analyzer v1.0

================================================

Target

https://example.com

Status Code

200

------------------------------------------------

Server

Apache/2.4.58

------------------------------------------------

Security Headers

✓ Strict-Transport-Security

✓ X-Frame-Options

✗ Content-Security-Policy

✗ Permissions-Policy

✗ Referrer-Policy

------------------------------------------------

Cookies

SESSIONID

✓ Secure

✗ HttpOnly

✗ SameSite

------------------------------------------------

HTML Report Generated

output/report.html
```

---

## 📄 HTML Report

The tool automatically generates a detailed HTML report containing:

- Scan information
- Target URL
- HTTP status code
- Server information
- Security header analysis
- Cookie analysis
- Overall security score
- Security grade

---

## 💡 Why This Project?

During web application penetration tests, checking HTTP security headers and cookie configurations is one of the first steps in identifying common security misconfigurations. While browsers and online tools can perform these checks, this project automates the process and generates a professional report that can be used during security assessments.

This project demonstrates:

- Python scripting
- Web security fundamentals
- HTTP protocol knowledge
- Report generation
- Security automation

---

## 🚧 Future Improvements

Planned enhancements include:

- CORS misconfiguration detection
- TLS/SSL analysis
- HTTP Methods (OPTIONS) analysis
- Clickjacking detection
- CSP policy analysis
- JSON report generation
- Technology fingerprinting
- CVE lookup for exposed server versions
- Screenshot capture
- OWASP ASVS checks

---

## 📸 Screenshots

### CLI Output

![Analyzer](/writeups/Screenshots/Http-Analyzer/Analyzer.png)

### HTML Report

![Reportr](/writeups/Screenshots/Http-Analyzer/report.png)

---

## 🤝 Contributing

Contributions, improvements, and feature suggestions are welcome. Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Balaji Murugesan**

- 🛡️ OSCP (OffSec Certified Professional)
- 🔐 Penetration Testing | Web Security | AI Security
- LinkedIn: [Balaji Murugesan](www.linkedin.com/in/balaji-murugesan-42447718a)
