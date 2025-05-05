def delete_info(conn):
    """Delete information from the Vault table with confirmation and SQL injection prevention"""
    
    serviceUrl = input("Enter service URL to delete: ").strip()

    # Ask the user for confirmation before proceeding with the deletion
    confirm = input(f"Are you sure you want to delete the record for service URL '{serviceUrl}'? (yes/no): ").strip().lower()

    if confirm != 'yes':
        print("Deletion cancelled.")
        return  # Exit without deleting if user doesn't confirm

    try:
        with conn.cursor() as cursor:
            # SQL query to delete record using a parameterized query
            deleteQuery = """
            DELETE FROM "Manager"."Vault" 
            WHERE "serviceURL" = %s
            """
            cursor.execute(deleteQuery, (serviceUrl,))
            conn.commit()

            # Check if the row was deleted
            if cursor.rowcount > 0:
                print(f"Record for service URL '{serviceUrl}' deleted successfully!")
            else:
                print(f"No record found for service URL '{serviceUrl}'.")

    except Exception as error:
        print(f"Error deleting data: {error}")