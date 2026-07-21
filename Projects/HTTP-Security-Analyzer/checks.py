import re

SECURITY_HEADERS = {

"Content-Security-Policy":
"Protects against XSS",

"Strict-Transport-Security":
"Forces HTTPS",

"X-Frame-Options":
"Clickjacking Protection",

"X-Content-Type-Options":
"MIME Sniffing Protection",

"Referrer-Policy":
"Controls Referrer Leakage",

"Permissions-Policy":
"Restricts Browser Features"

}

def check_headers(headers):

    results = []

    for header, purpose in SECURITY_HEADERS.items():

        if header in headers:

            results.append({

                "header": header,

                "status": "Present",

                "purpose": purpose,

                "risk": "Low"
                
                

            })

        else:

            results.append({

                "header": header,

                "status": "Missing",

                "purpose": purpose,

                "risk": "High"

            })

    return results

def analyze_cookies(response):

    cookies = []

    for cookie in response.cookies:

        cookies.append({

            "name": cookie.name,

            "secure": cookie.secure,

            "httponly": "HttpOnly" in str(cookie._rest),

            "samesite": get_samesite_value(cookie),
            
            "value": cookie.value

        })
        

    return cookies
    
# Search for and print "samesite="

def get_samesite_value(cookie):

    extra_attribute = cookie._rest
    samesite = next(
        (v for k, v in extra_attribute.items() if k.lower() == 'samesite'), 
        'Not Set'
    )

    return samesite
    

def check_server(headers):

    if "Server" in headers:

        return headers["Server"]

    return None
