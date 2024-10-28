import sqlite3

def create_user(username, password):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT
                    )''')
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def login(username, password):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user[0] if user else None  # Return user ID if found, else None

def signup():
    print("Create a new account:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    create_user(username, password)
    print("Account created successfully. You can now log in.")

def create_data_table():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_data (
                        data_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        data_value TEXT,
                        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                    )''')
    conn.commit()
    conn.close()

def list_items(user_id):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT data_value FROM user_data WHERE user_id = ?", (user_id,))
    items = cursor.fetchall()
    conn.close()
    
    if items:
        print("Your items:")
        for item in items:
            print(f"- {item[0]}")
    else:
        print("You have no items.")

def create_list(user_id):
    print("Creating a new list item:")
    data_value = input("Enter the item: ")
    
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_data (user_id, data_value) VALUES (?, ?)", (user_id, data_value))
    conn.commit()
    conn.close()
    print("Item created successfully.")

def main():
    create_data_table()  # Ensure the user_data table is created
    while True:
        print("\nChoose an option:")
        print("1. Login")
        print("2. Sign up")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user_id = login(username, password)
            if user_id:
                print("Login successful!")
                while True:
                    print("\nChoose an option:")
                    print("1. List items")
                    print("2. Create a new list")
                    print("3. Logout")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        list_items(user_id)
                    elif choice == "2":
                        create_list(user_id)
                    elif choice == "3":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid username or password.")

        elif choice == "2":
            signup()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
