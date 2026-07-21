import argparse
import requests


from colorama import Fore, Style, init
from checks import check_headers
from checks import analyze_cookies
from report import generate_report
#from checks import check_server

init(autoreset=True)

banner = r"""
 _   _ _____ _____ _____
| | | |_   _|_   _|  ___|
| |_| | | |   | | | |__
|  _  | | |   | | |  __|
| | | |_| |_  | | | |___
\_| |_/\___/  \_/ \____/

HTTP Security Analyzer v1.0
"""

print(Fore.CYAN + banner)

parser = argparse.ArgumentParser(
    description="HTTP Security Analyzer"
)

parser.add_argument(
    "-u",
    "--url",
    required=True,
    help="Target URL"
)

parser.add_argument(
    "--file",
    help="Filename (Default - report.html)"
)

args = parser.parse_args()

filename = "output/report.html"

if args.file:
   filename = f"output/{args.file}.html"


# Sends Request and parses the response

try:

    response = requests.get(
        args.url,
        timeout=10,
        verify=True
    )

except Exception as e:

    print(Fore.RED + str(e))
    exit()

print(Fore.GREEN + "\nTarget:", args.url)
print(Fore.GREEN + "Status:", response.status_code)
print()

print(Fore.YELLOW + "\033[4m" + "Response Headers\n" + "\033[0m")

for k, v in response.headers.items():

    print(f"{k}: {v}")
    
    
#Checks the security header
    
results = check_headers(response.headers)


print(Fore.YELLOW + "\033[4m" + "\nSecurity Headers\n" + "\033[0m")


for item in results:
     
    if item["status"] == "Present":
      for a, b in response.headers.items():
       if str(item.get("header", "")).lower() == a:
           print(
              Fore.GREEN +
              "[✓] "
              + item["header"] + ": " + b
           )

    else:

        print(
            Fore.RED +
            "[✗] "
            + item["header"]
        )

#Analyzing the cookies

cookies = analyze_cookies(response)

print(Fore.YELLOW + "\033[4m" + "\nCookies\n" + "\033[0m")


for cookie in cookies:

    print(cookie["name"] + ": " + cookie["value"])

    print(" Secure:", cookie["secure"])

    print(" HttpOnly:", cookie["httponly"])

    print(" SameSite:", cookie["samesite"])

    print()
    

from checks import check_server

server = check_server(response.headers)

print(Fore.YELLOW + "\033[4m" + "\nServer Information\n" + "\033[0m")

if server:

    print(Fore.GREEN + server)

else:

    print(Fore.GREEN + "No Server Banner")
    
generate_report(

    url=args.url,

    response=response,

    headers=results,

    cookies=cookies,

    server=server,
    
    output_file=filename

)    
 
