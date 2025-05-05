from initialize.encryptManager import decrypt_message

def retrieve_info(conn, fernet):
    """Retrieve and decrypt information from the Vault table"""
    serviceUrl = input("Enter service URL to retrieve: ").strip()

    try:
        with conn.cursor() as cursor:
            # SQL query to select record
            selectQuery = """
            SELECT "username", "password", "email"
            FROM "Manager"."Vault"
            WHERE "serviceURL" = %s
            """

            cursor.execute(selectQuery, (serviceUrl,))
            record = cursor.fetchone()

            if record:
                encUsername, encPassword, encEmail = record

                # Decrypt the data
                username = decrypt_message(encUsername, fernet)
                password = decrypt_message(encPassword, fernet)
                email = decrypt_message(encEmail, fernet)

                # Print out decrypted info
                print(f"\nDecrypted Information for {serviceUrl}:")
                print(f"Username: {username}")
                print(f"Password: {password}")
                print(f"Email: {email}")

            else:
                print(f"No record found for service URL: {serviceUrl}")

    except Exception as error:
        print(f"Error retrieving data: {error}")
