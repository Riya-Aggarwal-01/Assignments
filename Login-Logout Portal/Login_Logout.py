import sqlite3
import hashlib
import getpass

conn = sqlite3.connect("Login.db")
cursor = conn.cursor()
cursor.execute("""
         CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY NOT NULL,
            password TEXT NOT NULL,
            is_logged_in INTEGER DEFAULT 0
        ) """)
conn.commit()
conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    username = input("Enter new username: ").strip()
    if username == "":
        print("Cannot take empty value")
        return
    password = getpass.getpass("Enter your password: ").strip()
    if password == "":
        print("Password cannot be empty")
        return

    conn = sqlite3.connect("Login.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    if c.fetchone():
        print("Username already exists!")
    else:
        hashed = hash_password(password)
        c.execute("INSERT INTO users (username, password, is_logged_in) VALUES (?, ?, 0)", (username, hashed))
        conn.commit()
        print("Registered successfully!")

    conn.close()

def login():
    username = input("Enter your username").strip()
    if username == "":
        print("Cannot take empty value")
        return
    password = getpass.getpass("Enter your password: ").strip()
    conn = sqlite3.connect("Login.db")
    c = conn.cursor()

    hashed = hash_password(password)
    c.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
    result = c.fetchone()

    if not result:
        print("User does not exist!")
    elif result[1] == 1:
        print("User already logged in!")
    elif result[0] == hashed:
        c.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (username,))
        conn.commit()
        print("Login successful!")
    else:
        print("Incorrect password!")

def logout():
    username = input("Enter username to logout: ").strip()
    if username == "":
        print("Cannot take empty value")
        return

    conn = sqlite3.connect("Login.db")
    c = conn.cursor()

    c.execute("SELECT is_logged_in FROM users WHERE username = ?", (username,))
    result = c.fetchone()

    if not result:
        print("User not found!")
    elif result[0] == 0:
        print("User is not logged in!")
    else:
        c.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (username,))
        conn.commit()
        print("Logout successful!")

    conn.close()

def change_password():
    username = input("Enter username: ").strip()
    if username == "":
        print("Cannot take empty value")
        return
    old_password = getpass.getpass("Enter your current password: ").strip()

    conn = sqlite3.connect("Login.db")
    c = conn.cursor()

    hashed_old = hash_password(old_password)
    c.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
    result = c.fetchone()

    if not result:
        print("User does not exist!")
    elif result[1] == 0:
        print("You must be logged in to change password!")
    elif result[0] != hashed_old:
        print("Incorrect current password!")
    else:
        new_password = getpass.getpass("Enter new password: ").strip()
        confirm_pass = getpass.getpass("Confirm new password: ").strip()

        if new_password != confirm_pass:
            print("Passwords do not match.")
            return
        hashed_new = hash_password(new_password)
        c.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_new, username))
        conn.commit()
        print("Password updated successfully!")

    conn.close()


while True:
        print("\n-- Portal --")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Change Password")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            change_password()
        elif choice == "5":
            conn = sqlite3.connect("Login.db")
            c = conn.cursor()
            c.execute("UPDATE users SET is_logged_in = 0")
            conn.commit()
            conn.close()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

