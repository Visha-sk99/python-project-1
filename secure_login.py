import os

# File to store credentials
USER_FILE = "users.txt"
def check_password_strength(password):
    if len(password) < 8 or len(password) > 12:
        return False, "Password must be between 8 and 12 characters."

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_+=" for c in password)

    if all([has_upper, has_lower, has_digit, has_special]):
        return True, "Strong password."
    else:
        return False, "Password must include uppercase, lowercase, digit, and special character."
def register_user():
    username = input("Enter username: ")

    # Check if username exists
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                if line.split(",")[0] == username:
                    print("❌ Username already exists.")
                    return

    password = input("Enter password: ")
    valid, message = check_password_strength(password)
    if not valid:
        print(f"❌ {message}")
        return

    with open(USER_FILE, "a") as file:
        file.write(f"{username},{password}\n")
    print("✅ Registration successful!")
def login_user():
    if not os.path.exists(USER_FILE):
        print("❌ No users registered yet!")
        return

    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(USER_FILE, "r") as file:
        for line in file:
            user, pwd = line.strip().split(",")
            if user == username and pwd == password:
                print("✅ Login successful! Welcome,", username)
                return

    print("❌ Invalid username or password.")
def menu():
    while True:
        print("\n=== Secure Login System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    menu()
