INTERESTING_PORTS = {
    21: {
        "service": "FTP",
        "risk": "Anonymous login, weak credentials",
        "tools": ["ftp", "hydra", "nmap ftp-*"]
    },
    22: {
        "service": "SSH",
        "risk": "Weak credentials",
        "tools": ["hydra", "ssh-audit"]
    },
    80: {
        "service": "HTTP",
        "risk": "Web Application",
        "tools": ["whatweb", "ffuf", "nikto"]
    },
    139: {
        "service": "NetBIOS",
        "risk": "SMB Enumeration",
        "tools": ["enum4linux-ng", "smbclient"]
    },
    443:{
    	"service": "HTTPS",
        "risk": "SMB Enumeration",
        "tools": ["whatweb", "ffuf", "nikto"]
    },
    445: {
        "service": "SMB",
        "risk": "SMB Enumeration",
        "tools": ["enum4linux-ng", "smbclient", "crackmapexec"]
    },
    3389: {
        "service": "RDP",
        "risk": "Remote Desktop",
        "tools": ["xfreerdp", "hydra"]
    },
    5985: {
        "service": "WinRM",
        "risk": "Remote Management",
        "tools": ["evil-winrm", "crackmapexec"]
    },
    3306: {
        "service": "MySQL",
        "risk": "Database",
        "tools": ["mysql", "nmap mysql-*"]
    },
    1433: {
        "service": "MSSQL",
        "risk": "Database",
        "tools": ["impacket-mssqlclient"]
    }
}


def analyze_ports(scanner):
    findings = []

    for host in scanner.all_hosts():

        for proto in scanner[host].all_protocols():

            for port in scanner[host][proto]:

                if port in INTERESTING_PORTS:

                    info = INTERESTING_PORTS[port]

                    findings.append({
                        "host": host,
                        "port": port,
                        "service": info["service"],
                        "risk": info["risk"],
                        "tools": info["tools"]
                    })

    return findings
