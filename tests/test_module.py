# Automated tests
# NOTE: I already put a single fixed user input for each test case to reference on

import pytest
from src.module import UserValidator

def test_register_positive():
    auth = UserValidator()
    assert auth.register_user("user123", "password123") is True

def test_register_negative_short_password():
    auth = UserValidator()
    with pytest.raises(ValueError, match="Password must be at least 8 characters"):
        auth.register_user("user123", "short")

def test_register_negative_invalid_chars():
    auth = UserValidator()
    with pytest.raises(ValueError, match="Username must be alphanumeric"):
        auth.register_user("user!@#", "password123")

def test_register_edge_duplicate():
    auth = UserValidator()
    auth.register_user("user1", "password123")
    with pytest.raises(ValueError, match="User already exists"):
        auth.register_user("user1", "password123")

