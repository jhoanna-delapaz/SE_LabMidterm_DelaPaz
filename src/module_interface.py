# Module: User authentication validator (Interface)
from module import UserValidator

def main():
    auth = UserValidator()

    while True:
        print("\n--- User Authentication System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            user = input("Enter username: ")
            pw = input("Enter password: ")
            try:
                auth.register_user(user, pw)
                print("Registration successful!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            user = input("Enter username: ")
            pw = input("Enter password: ")
            if auth.validate_login(user, pw):
                print("Login successful! Welcome.")
            else:
                print("Login failed. Incorrect credentials.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()