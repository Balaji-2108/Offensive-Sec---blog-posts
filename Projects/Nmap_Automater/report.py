import os
from datetime import datetime


def generate_html_report(scanner, findings, filename):

    html = f"""
    <html>

    <head>

    <title>Nmap Report</title>

    <style>

    body {{
        font-family: Arial;
        margin:40px;
        background:#f8f8f8;
    }}

    table {{
        border-collapse:collapse;
        width:100%;
    }}

    th,td {{
        border:1px solid #ddd;
        padding:10px;
    }}

    th {{
        background:#222;
        color:white;
    }}

    h1 {{
        color:#222;
    }}

    </style>

    </head>

    <body>

    <h1>Nmap Automation Report</h1>

    <p>Generated: {datetime.now()}</p>
    """

    for host in scanner.all_hosts():

        html += f"<h2>Host: {host}</h2>"

        html += f"<p>Status: {scanner[host].state()}</p>"

        html += """
        <table>

        <tr>

        <th>Port</th>
        <th>State</th>
        <th>Service</th>
        <th>Version</th>

        </tr>
        """

        for proto in scanner[host].all_protocols():

            for port in scanner[host][proto]:

                service = scanner[host][proto][port]

                version = (
                    service.get("product", "")
                    + " "
                    + service.get("version", "")
                )

                html += f"""

                <tr>

                <td>{port}</td>

                <td>{service['state']}</td>

                <td>{service['name']}</td>

                <td>{version}</td>

                </tr>

                """

        html += "</table>"

    html += "<h2>Interesting Findings</h2>"

    html += """

    <table>

    <tr>

    <th>Host</th>

    <th>Port</th>

    <th>Service</th>

    <th>Risk</th>

    <th>Recommended Tools</th>

    </tr>

    """

    for finding in findings:

        html += f"""

        <tr>

        <td>{finding['host']}</td>

        <td>{finding['port']}</td>

        <td>{finding['service']}</td>

        <td>{finding['risk']}</td>

        <td>{', '.join(finding['tools'])}</td>

        </tr>

        """

    html += """

    </table>

    </body>

    </html>

    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, "w") as f:
        f.write(html)

    print(f"\n[+] Report saved to {filename}")
