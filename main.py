import string
import secrets


def generate_password(length=64):
    # Define the characters that will be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # Ensure the password includes at least one character from each category
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    # Fill the rest of the password length with random characters
    for i in range(length - 4):
        password.append(secrets.choice(all_characters))
    # Shuffle the list of characters
    secrets.SystemRandom().shuffle(password)
    # Convert the list of characters into a string
    password = ''.join(password)
    return password


# Generate a 64-character password
print(generate_password())

# Keep the script running
while True:
    input("Press enter to generate a new password.")
    print(generate_password())