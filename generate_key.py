import json
import os
import random
import string

LICENSE_FILE = "licenses.json"

def load_licenses():
    if not os.path.exists(LICENSE_FILE):
        return {}
    with open(LICENSE_FILE, "r") as f:
        return json.load(f)

def save_licenses(data):
    with open(LICENSE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_key():
    parts = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(3)]
    return '-'.join(parts)

def add_license(uuid):
    licenses = load_licenses()
    while True:
        key = generate_key()
        if key not in licenses:
            break
    licenses[key] = {
        "status": "active",
        "uuid": uuid
    }
    save_licenses(licenses)
    print(f"تم توليد المفتاح: {key} لـ UUID: {uuid}")

if name == "main":
    uuid_input = input("أدخل UUID الجهاز: ").strip()
    add_license(uuid_input)
