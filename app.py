from flask import Flask, request, jsonify
import json
import os

app = Flask(name)

LICENSE_FILE = "licenses.json"

# تحميل التراخيص من ملف JSON
def load_licenses():
    if not os.path.exists(LICENSE_FILE):
        return {}
    with open(LICENSE_FILE, "r") as f:
        return json.load(f)

@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    key = data.get("key")
    uuid = data.get("uuid")

    licenses = load_licenses()
    license_data = licenses.get(key)

    if not license_data:
        return jsonify({"status": "invalid", "message": "Key not found"})

    if license_data["status"] != "active":
        return jsonify({"status": "blocked", "message": "Key is not active"})

    if license_data["uuid"] != uuid:
        return jsonify({"status": "unauthorized", "message": "UUID mismatch"})

    return jsonify({"status": "valid", "message": "License verified"})

if name == "main":
    app.run(host="0.0.0.0", port=5000)
