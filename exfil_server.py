from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

RECEIVED_LOG = "logs/received_exfil_data.bin"

@app.route("/exfil", methods=["POST"])
def receive_data():
    encrypted_data = request.data

    if not encrypted_data:
        return "No data received", 400

    with open(RECEIVED_LOG, "ab") as f:
        f.write(b"\n--- " + str(datetime.now()).encode() + b" ---\n")
        f.write(encrypted_data)

    return "Data received securely", 200

if __name__ == "__main__":
    print("[+] Local Exfiltration Server Running")
    print("[+] Listening on http://127.0.0.1:5000/exfil")
    app.run(host="127.0.0.1", port=5000)
