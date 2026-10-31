import re

def validate_mac(mac):
    pattern = r"^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$"

    if re.match(pattern, mac):
        return True
    return False


print("===== MAC ADDRESS VALIDATOR =====")

mac = input("Enter MAC Address: ").strip()

if validate_mac(mac):
    print("Valid MAC Address")
else:
    print("Invalid MAC Address")