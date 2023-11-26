import string
import secrets


def generate_password(length=100):
    # Define the characters that will be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # Fill the password length with random characters
    password = [secrets.choice(all_characters) for _ in range(length)]
    # Shuffle the list of characters
    secrets.SystemRandom().shuffle(password)
    # Convert the list of characters into a string
    password = ''.join(password)
    return password


# Generate a 100-character password
print(generate_password())

# Keep the script running
while True:
    input("Press enter to generate a new password.")
    print(generate_password())