from initialize.encryptManager import encrypt_message

def modify_info(conn, fernet):
    """Modify information in the Vault table"""

    serviceUrl = input("Enter service URL to modify: ").strip()
    newUsername = input("Enter new username: ").strip()
    newPassword = input("Enter new password: ").strip()
    newEmail = input("Enter new email: ").strip()

    # Encrypt sensitive data
    encUsername = encrypt_message(newUsername, fernet)
    encPassword = encrypt_message(newPassword, fernet)
    encEmail = encrypt_message(newEmail, fernet)

    try:
        with conn.cursor() as cursor:
            update_query = """
            UPDATE "Manager"."Vault"
            SET "username" = %s, "password" = %s, "email" = %s
            WHERE "serviceURL" = %s
            """
            cursor.execute(update_query, (encUsername, encPassword, encEmail, serviceUrl))
            conn.commit()
            print(f"Record for {serviceUrl} updated successfully!")
    except Exception as error:
        print(f"Error modifying data: {error}")