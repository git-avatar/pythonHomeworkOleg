password = input("Enter your password (must contain: 8+ characters, 1 digit, 1 lowercase, 1 uppercase): ")
user = input("Enter your username (must contain: 1 lower,1 upper, 6+ characters): ")

pass_len = len(password)
user_len = len(user)

has_lowercase = any(char.islower() for char in password)
has_uppercase = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)

if user_len >= 6 and pass_len >= 8 and has_lowercase and has_uppercase and has_digit:
    print("Login is successful.")
else:
    print("Login is not successful.")
if user_len < 6:
    print("Your character must contain 6 or more characters!")
if pass_len < 8:
    print("Your password must contain 8 or more characters!")
if not any(char.islower() for char in password):
    print("You must have at least one lowercase letter in your password!")
if not any(char.isupper() for char in password):
    print("You must have at least one uppercase letter in your password!")
if not any(char.isdigit() for char in password):
    print("You must have at least 1 digit in your password!")


if not any(char.islower() for char in user):
    print("You must have at least 1 lowercase letter in your username!")
if not any(char.isupper() for char in user):
    print("You must have at least 1 uppercase letter in your username!")