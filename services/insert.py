from initialize.encryptManager import encrypt_message

def insert_info(conn, fernet):
    """Insert information into the Vault table"""

    serviceUrl = input("Enter service URL: ").strip()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    email = input("Enter email: ").strip()

    # Encrypt sensitive data
    encUsername = encrypt_message(username, fernet)
    encPassword = encrypt_message(password, fernet)
    encEmail = encrypt_message(email, fernet)

    try:
        with conn.cursor() as cursor:
            insert_query = """
            INSERT INTO "Manager"."Vault" ("serviceURL", "username", "password", "email")
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (serviceUrl, encUsername, encPassword, encEmail))
            conn.commit()
            print("Record inserted successfully!")
    except Exception as error:
        print(f"Error inserting data: {error}")