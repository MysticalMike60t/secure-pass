import string
import secrets

# ANSI escape codes for some colors
COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m',
}


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


try:
    # Generate a 100-character password
    print(COLORS['cyan'] + generate_password() + COLORS['reset'])

    # Keep the script running
    while True:
        input("Press enter to generate a new password.")
        print(COLORS['cyan'] + generate_password() + COLORS['reset'])
except KeyboardInterrupt:
    print("\n" + COLORS['red'] + "Generator Stopped" + COLORS['reset'])