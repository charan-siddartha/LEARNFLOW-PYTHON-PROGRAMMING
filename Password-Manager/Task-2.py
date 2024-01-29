

pip install cryptography


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode
import json
import os
import string
import random

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.passwords = {}

    def _derive_key(self, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(self.master_password.encode())
        return key

    def _encrypt(self, plaintext, key, nonce):
        cipher = Cipher(algorithms.AES(key), modes.CFB(nonce), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
        return ciphertext

    def _decrypt(self, ciphertext, key, nonce):
        cipher = Cipher(algorithms.AES(key), modes.CFB(nonce), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext.decode()

    def _save_passwords(self):
        # Convert tuple keys to strings
        converted_passwords = {str(key): value for key, value in self.passwords.items()}
        
        with open('passwords.json', 'w') as file:
            file.write(json.dumps(converted_passwords))

    def _load_passwords(self):
        if os.path.exists('passwords.json'):
            with open('passwords.json', 'r') as file:
                converted_passwords = json.load(file)
                # Convert keys back to tuples
                self.passwords = {tuple(key): value for key, value in converted_passwords.items()}

    def generate_strong_password(self, length=16):
        symbols = '#@$&*'
        chars = string.ascii_letters + string.digits + symbols
        password = ''.join(random.choice(chars) for _ in range(length))
        return password

    def add_password(self, category, service, username):
        password = self.generate_strong_password()
        salt = os.urandom(16)
        key = self._derive_key(salt)
        nonce = os.urandom(16)
        encrypted_password = self._encrypt(password, key, nonce)
        self.passwords[(category, service)] = {'username': username, 'salt': urlsafe_b64encode(salt).decode(),
                                               'nonce': urlsafe_b64encode(nonce).decode(),
                                               'password': urlsafe_b64encode(encrypted_password).decode()}
        self._save_passwords()
        return password

    def get_password(self, category, service):
        if (category, service) in self.passwords:
            entry = self.passwords[(category, service)]
            salt = urlsafe_b64decode(entry['salt'])
            key = self._derive_key(salt)
            nonce = urlsafe_b64decode(entry['nonce'])
            encrypted_password = urlsafe_b64decode(entry['password'])
            password = self._decrypt(encrypted_password, key, nonce)
            return password
        else:
            return None

# Example Usage
master_password = input("Enter your master password: ")
password_manager = PasswordManager(master_password)

# Add passwords
password_manager.add_password("Email", "Gmail", "user@gmail.com")
password_manager.add_password("Banking", "XYZ Bank", "account123")

# Retrieve passwords
email_password = password_manager.get_password("Email", "Gmail")
bank_password = password_manager.get_password("Banking", "XYZ Bank")

print("Email Password:", email_password)
print("Banking Password:", bank_password)


# In[ ]:



