def is_strong_password(password):
    # Minimum length check
    if len(password) < 8:
        return False
    
    # Uppercase letter check
    if not any(char.isupper() for char in password):
        return False
    
    # Lowercase letter check
    if not any(char.islower() for char in password):
        return False
    
    # Digit check
    if not any(char.isdigit() for char in password):
        return False

    # If all criteria are met, the password is considered strong
    return True

# Example usage:
password_to_check = input("Enter your password: ")
if is_strong_password(password_to_check):
    print("Your password is strong!")
else:
    print("Your password is not strong. Please follow the recommended criteria.")
