import argparse
import nmap
import os

from parser import analyze_ports
from report import generate_html_report

banner = r"""

███╗   ██╗███╗   ███╗ █████╗ ██████╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗
██╔██╗ ██║██╔████╔██║███████║██████╔╝
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝


"""

print(banner)

scanner = nmap.PortScanner()

parser = argparse.ArgumentParser(
    description="Nmap Automator - Automated Recon Tool"
)

parser.add_argument(
    "-t",
    "--target",
    required=True,
    help="Target IP, Hostname, or CIDR"
)

parser.add_argument(
    "--port",
    help="Specific port scan"
)

parser.add_argument(
    "--quick",
    action="store_true",
    help="Quick scan (Top 1000 ports)"
)

parser.add_argument(
    "--full",
    action="store_true",
    help="Full TCP port scan"
)

parser.add_argument(
    "--ping",
    action="store_true",
    help="Ping sweep only"
)

parser.add_argument(
    "--file",
    action="store_true",
    help="Provide filename"
)


args = parser.parse_args()

scanner = nmap.PortScanner()

scan_name = f"output/{args.target}.html"

scan_args = "-sV -sC"

if args.full:
    scan_args = "-vv -Pn -p-"

if args.quick:
    scan_args += " -T4"

if args.ping:
    scan_args = "-sn"

if args.port:
    scan_args = f"-sCV -p {args.port}"

if args.file:
    scan_name = f"output/{args.file}.html"

print(f"[+] Target : {args.target}")
print(f"[+] Arguments : {scan_args}")
print("[+] Scanning...\n")

scanner.scan(
    hosts=args.target,
    arguments=scan_args
)


for host in scanner.all_hosts():

    print("="*50)
    print(f"Host: {host}")
    print(f"State: {scanner[host].state()}")

    for proto in scanner[host].all_protocols():

        print(f"\nProtocol: {proto}")

        ports = scanner[host][proto].keys()

        for port in sorted(ports):

            service = scanner[host][proto][port]

            print(
                f"{port}/tcp "
                f"{service['state']} "
                f"{service['name']} "
                f"{service.get('product','')} "
                f"{service.get('version','')}"
            )

findings = analyze_ports(scanner)

print("\nInteresting Findings\n")

for finding in findings:

    print(f"[+]{finding['service']} ({finding['port']})")
    print(f"    Risk : {finding['risk']}")
    print(f"    Tools: {', '.join(finding['tools'])}")
    print()
    
    
generate_html_report(scanner, findings, scan_name)
