import re

def validate_ipv4(ip):
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"

    if re.match(pattern, ip):
        return True
    return False


print("===== IPv4 ADDRESS VALIDATOR =====")

ip = input("Enter IPv4 Address: ").strip()

if validate_ipv4(ip):
    print("Valid IPv4 Address")
else:
    print("Invalid IPv4 Address")