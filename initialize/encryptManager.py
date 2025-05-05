from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

# Generate a Fernet key from master password
def generate_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

# Encrypt a plaintext string
def encrypt_message(message: str, fernet: Fernet) -> str:
    return fernet.encrypt(message.encode()).decode()

# Decrypt a ciphertext string
def decrypt_message(token: str, fernet: Fernet) -> str:
    return fernet.decrypt(token.encode()).decode()