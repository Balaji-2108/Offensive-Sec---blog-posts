from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os


def generate_report(
        url,
        response,
        headers,
        cookies,
        server,
        output_file):

    os.makedirs("output", exist_ok=True)

    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template("report.html")

    html = template.render(

        date=datetime.now(),

        url=url,

        status=response.status_code,

        headers=headers,

        cookies=cookies,

        server=server

    )

    with open(output_file, "w", encoding="utf-8") as f:

        f.write(html)

    print(f"\n[+] Report saved to {output_file}")
