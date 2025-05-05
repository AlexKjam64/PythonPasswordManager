from initialize.encryptManager import generate_key
from cryptography.fernet import Fernet
import os

def store_master_password(input_password, salt):
    """Store an encrypted version of the master password"""
    
    # Generate key using the input password and the salt
    key = generate_key(input_password, salt)
    fernet = Fernet(key)
    
    # Encrypt the master password and store it in a file
    encrypted_master_password = fernet.encrypt(input_password.encode())
    
    with open("initialize/encrypted_master_password.bin", "wb") as f:
        f.write(encrypted_master_password)

    print("Master password has been securely stored.")

def verify_master_password(input_password, salt):
    """Verify the master password by comparing with the stored one"""
    
    # Generate key using the input password and the salt
    key = generate_key(input_password, salt)
    fernet = Fernet(key)

    # Check if the generated key matches the stored encrypted master password
    if os.path.exists("initialize/encrypted_master_password.bin"):
        with open("initialize/encrypted_master_password.bin", "rb") as f:
            stored_encrypted_master_password = f.read()

        try:
            # Try decrypting the stored master password with the generated key
            fernet.decrypt(stored_encrypted_master_password)
            return True 
        except:
            return False
    else:
        return False