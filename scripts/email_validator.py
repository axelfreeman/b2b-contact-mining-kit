#!/usr/bin/env python3
\"\"\"
Simple SMTP email validator — checks if an email address exists without sending.
Usage: python email_validator.py emails.txt
\"\"\"
import smtplib
import dns.resolver
import sys

def verify_email(email):
    domain = email.split('@')[1]
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx = str(records[0].exchange)
        server = smtplib.SMTP(timeout=10)
        server.connect(mx)
        server.helo()
        server.mail('test@example.com')
        code, _ = server.rcpt(email)
        server.quit()
        return code == 250
    except:
        return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python email_validator.py emails.txt")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        for email in f:
            email = email.strip()
            if email:
                valid = verify_email(email)
                status = "VALID" if valid else "INVALID" if valid is False else "UNKNOWN"
                print(f"{status}: {email}")
