import string


# Password Strength Checker
# Define a function that checks if a password meets criteria (length, digit, symbol, upper case).


def is_password_strong(password):
    has_digit = False
    has_upper = False
    has_symbol = False

    if len(password) < 8:
        return "Password to short"
    
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char in string.punctuation:
            has_symbol = True

    if has_digit and has_upper and has_symbol :
        return "Strong Passwor"
    else:
        return "Weak Password"
    

password_check = is_password_strong("Kahajf56@")
print(password_check)