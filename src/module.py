# Module: User authentication validator (Logic)
class UserValidator:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        # Username must not contain special characters
        if not username.isalnum():
            raise ValueError("Username must be alphanumeric.")

        # Enforce minimum password length
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        # Prevent duplicate registrations
        if username in self.users:
            raise ValueError("User already exists.")

        # Store user data and return
        self.users[username] = password
        return True

    # Check if username exists in records
    def validate_login(self, username, password):
        if username not in self.users:
            return False
        # Verify if the password matches the stored one
        return self.users[username] == password