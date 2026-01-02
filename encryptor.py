from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    """
    Generates a key and saves it into a file
    """
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

def load_key():
    """
    Loads the key from the current directory
    """
    return open(KEY_FILE, "rb").read()

def encrypt_data(data: str) -> bytes:
    """
    Encrypts plaintext data
    """
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data.encode())
    return encrypted

def decrypt_data(encrypted_data: bytes) -> str:
    """
    Decrypts encrypted data (for demo/testing only)
    """
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data)
    return decrypted.decode()

# Generate key on first run
generate_key()
