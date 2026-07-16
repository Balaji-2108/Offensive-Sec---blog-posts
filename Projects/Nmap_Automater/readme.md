# Nmap Automator 👁️

An automated **Python-based Nmap reconnaissance tool** that performs network scanning, parses results, identifies interesting services, and generates a professional HTML report with recommended next steps for penetration testers.

This project was built to automate the initial reconnaissance phase of a penetration test and reduce the manual effort involved in analyzing Nmap scan results.

---

## ✨ Features

- 🔍 Automated Nmap scanning
- ⚡ Quick and Full scan modes
- 🌐 Supports single IP, hostname, and CIDR ranges
- 📄 Generates HTML reports
- 📁 Saves Nmap output in XML, GNMAP, and NMAP formats
- 🚨 Detects interesting services automatically
- 🛠️ Recommends enumeration tools based on discovered services
- 📂 Custom output directory support
- 💻 Professional command-line interface (CLI)

---

## 📂 Project Structure

```
Nmap-Automator/
│
├── scanner.py          # Main scanner
├── parser.py           # Port analysis & recommendations
├── report.py           # HTML report generator
├── output/
│   ├── report.html
│   ├── scan.xml
│   ├── scan.nmap
│   └── scan.gnmap
│
├── requirements.txt
└── README.md
```

---

## 🛠 Requirements

- Python 3.10+
- Nmap

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

Install Nmap

**Ubuntu/Kali**

```bash
sudo apt install nmap
```

Verify installation

```bash
nmap --version
```

---

## 🚀 Usage

### Quick Scan

```bash
python3 scanner.py -t 192.168.1.10 --quick
```

---

### Full Scan

```bash
python3 scanner.py -t 192.168.1.10 --full
```

---

### Ping Sweep

```bash
python3 scanner.py -t 192.168.1.0/24 --ping
```

---

### Custom Output Directory

```bash
python3 scanner.py -t 192.168.1.10 -o reports
```

---

## ⚙️ Available Options

| Option | Description |
|---------|-------------|
| `-t` | Target IP, Hostname or CIDR |
| `--quick` | Quick service scan |
| `--full` | Scan all TCP ports |
| `--ping` | Host discovery only |
| `-o` | Output directory |
| `-h` | Display help |

---

## 📄 Generated HTML Report

The tool generates a clean HTML report containing:

- Scan summary
- Host status
- Open ports
- Service versions
- Interesting findings
- Risk descriptions
- Recommended enumeration tools

---

## 🎯 Interesting Service Detection

The tool automatically detects commonly targeted services such as:

| Port | Service |
|------|----------|
| 21 | FTP |
| 22 | SSH |
| 80 | HTTP |
| 139 | NetBIOS |
| 445 | SMB |
| 3389 | RDP |
| 5985 | WinRM |
| 3306 | MySQL |
| 1433 | MSSQL |

---

### Planned Features

- 🔍 CVE lookup using NVD API
- 📊 Risk scoring
- 🎨 Beautiful Bootstrap HTML reports
- 📸 Automatic website screenshots
- 📄 JSON export
- 🌈 Colored CLI output
- 📈 Scan statistics dashboard
- 🧠 AI-powered enumeration suggestions
- 📦 Docker support

---

## 🤝 Contributing

Contributions, feature requests, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

**Balaji Murugesan**

- OSCP (OffSec Certified Professional)
- Cybersecurity | Penetration Testing | AI Security
- LinkedIn: https://www.linkedin.com/in/<your-profile>
- GitHub: https://github.com/Balaji-2108
