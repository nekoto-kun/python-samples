# Import libraries
import sqlite3

# Vulnerable function
def get_user_data(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id};"
    connection = sqlite3.connect("samples/user.sqlite")
    cursor = connection.cursor()

    cursor.execute(query)
    user_data = cursor.fetchall() # Fetch all rows

    cursor.close()
    connection.close()

    return user_data

# Attack scenario
print("Vulnerable function")
user_id = "1 OR 1=1"
user_data = get_user_data(user_id)
print(user_data)

# Protection
def get_user_data_protected(user_id):
    query = f"SELECT * FROM users WHERE id = ?;"
    connection = sqlite3.connect("samples/user.sqlite")
    cursor = connection.cursor()

    cursor.execute(query, (user_id,)) # Pass the user_id as a tuple
    # user_data = cursor.fetchall()
    user_data = cursor.fetchone() # Fetch only one row

    cursor.close()
    connection.close()

    return user_data

# Attack scenario
print("\nProtected function")
user_id = "1 OR 1=1"
user_data = get_user_data_protected(user_id)
print(user_data)