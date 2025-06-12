import os
from cryptography.fernet import Fernet

CONFIG_FILE = "secret.key"

def load_or_create_key():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open(CONFIG_FILE, "wb") as key_file:
            key_file.write(key)
        print("Nueva clave generada y guardada.")
    
    return Fernet(key)

fernet = load_or_create_key()
