🔐 Keylogger with Encrypted Data Exfiltration

📌 Project Description

This project is a defensive cybersecurity lab that demonstrates how keylogging behavior and outbound data exfiltration attempts can be detected, validated, and logged in a controlled and ethical environment.

The project focuses on security awareness, detection, and monitoring, not exploitation.

---

🎯 Project Objectives

Demonstrate how keylogging techniques work at a conceptual and educational level

Simulate outbound data exfiltration attempts

Observe server-side input validation and rejection

Analyze logs as attack indicators

---

🧱 Project Structure

keylogger-lab/

├── venv/  # Python virtual environment

├── keylogger.py             # Ethical keylogger (local, user-controlled)

├── exfil_server.py          # Flask-based exfiltration detection server

├── logs/

│   ├── encrypted_logs.bin

├── kill_switch.txt          # Safety stop mechanism

├── requirements.txt         # Python dependencies

└── README.md                # Project documentation

---

🔁 Project Workflow

1. The ethical keylogger is executed manually

2. Keystrokes are captured locally for testing

3. A simulated outbound transfer is attempted

---

▶️ How to Execute the Project

🔹 Prerequisites

Python 3.8 or higher

Linux or Windows

Virtual environment support

 Step 1: Clone the Repository

    https://github.com/Harishwar006/keylogger-with-encrypted-data-exfiltration/tree/main

    cd keylogger-with-encrypted-data-exfiltration

 Step 2: Create and Activate Virtual Environment

Linux / Kali / Ubuntu

    python3 -m venv venv

    source venv/bin/activate

Windows (PowerShell)

    python -m venv venv

    venv\Scripts\activate
    
 Step 3: Install Dependencies

    pip install -r requirements.txt

 Step 4: Start the Exfiltration Detection Server

    python exfil_server.py

Server will start on:

    http://127.0.0.1:5000

Leave this terminal running.

 Step 5: Run the Ethical Keylogger (New Terminal)

Open a new terminal, activate the virtual environment again, then run:

     rm kill_switch.txt

    python keylogger.py

> The keylogger runs only locally and requires manual execution.

 Step 6: Stop the Project

Press: (Exfiltration side)

CTRL + C

create the kill switch file (New Terminal) for Keylogger:

    touch kill_switch.txt

 Step 7: Deactivate Virtual Environment

    deactivate

 Step 8: To view encrypted text

   open project file --> logs --> encrypted_log.bin
   
---

✅ Expected Behavior

Server returns 400 / 404 for invalid requests

No real data is accepted

System remains secure

---

📊 HTTP Response Behavior

Status Code	Description

404	Undefined route access blocked

400	Invalid or malformed data rejected

403	Access forbidden (if enforced)

500	Server error (not expected)

Correct operation results in rejected requests, not accepted data.

---

🛑 Kill Switch

A kill_switch.txt file is included as a safety control:

Instantly stops logging activity

Prevents accidental misuse

Demonstrates fail-safe design

---

✅ Conclusion

This project demonstrates how:

Keylogging threats are understood

Exfiltration attempts are detected

Security controls reject unsafe behavior

Logs provide actionable security insight

Blocked attacks indicate successful defense.

---

