from initialize.initializeConnection import initialize_con
from initialize.encryptManager import generate_key
from services.verify import verify_master_password
from services.verify import store_master_password
from services.insert import insert_info
from services.delete import delete_info
from services.modify import modify_info
from services.retrieve import retrieve_info
from cryptography.fernet import Fernet
import getpass
import os

def main():
    print("* * * * * * * *\nWelcome to the password manager!\n* * * * * * * *")

    # Get master password (DON'T LOSE MASTER PASSWORD!!!)
    master_password = getpass.getpass("Enter your master password: ")

    # Load or create salt (MAKE SURE YOU USE SAME FILE FOR ENCRYPTING/DECRYPTING FILES!!!)
    if not os.path.exists("initialize/salt.bin"):
        salt = os.urandom(16)
        with open("initialize/salt.bin", "wb") as f:
            f.write(salt)
    else:
        with open("initialize/salt.bin", "rb") as f:
            salt = f.read()

    # If there's no encrypted password stored, this is the first setup
    if not os.path.exists("initialize/encrypted_master_password.bin"):
        print("No stored master password found. Setting up a new one.")
        store_master_password(master_password, salt)
    else:
        # Verify master password
        if not verify_master_password(master_password, salt):
            print("Invalid master password! Exiting application.")
            return  # Exit if the password is incorrect

    key = generate_key(master_password, salt)
    fernet = Fernet(key)

    # Establish the database connection
    conn = initialize_con()

    actions = {
        'a': lambda conn: insert_info(conn, fernet),
        'd': delete_info,
        'm': lambda conn: modify_info(conn, fernet),
        'r': lambda conn: retrieve_info(conn, fernet)
    }
    
    # Select an option in the menu
    userInput = None
    while(userInput != 'q'):
        print("\n- - - - - - - -\nPlease select an action:")
        print("a - insert information")
        print("d - delete information")
        print("m - modify information")
        print("r - retrieve information")
        print("q - quit application")
        userInput = input().strip().lower()

        if userInput == 'q':
            print("Exiting the application...")
        elif userInput in actions:
            actions[userInput](conn)
        else:
            print("Invalid input, please try again!")
    
    if conn:
        conn.close()
        print("Database connection closed.")

if __name__ == '__main__':
    main()