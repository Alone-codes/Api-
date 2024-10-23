import sqlite3


def create_user(username, password):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT,
                        password TEXT
                    )''')
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()


def login(username, password):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None


def signup():
    print("Create a new account:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    create_user(username, password)
    print("Account created successfully. You can now log in.")


def list_items():
    print("your old items : ")
    1

def create_list():
    print("Creating a new list:")
   

def main():
    while True:
        print("\nChoose an option:")
        print("1. Login")
        print("2. Sign up")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if login(username, password):
                print("Login successful!")
                while True:
                    print("\nChoose an option:")
                    print("1. List items")
                    print("2. Create a new list")
                    print("3. Logout")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        list_items()
                    elif choice == "2":
                        create_list()
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
