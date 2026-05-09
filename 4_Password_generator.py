import secrets
import string

MIN_LENGTH = 8
MAX_LENGTH = 64

def generate_password(length: int) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

def get_password_length() -> int:
    while True:
        try:
            length = int(input(f"Enter password length ({MIN_LENGTH}–{MAX_LENGTH}): "))
            if MIN_LENGTH <= length <= MAX_LENGTH:
                return length
            print(f"Please enter a value between {MIN_LENGTH} and {MAX_LENGTH}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    length = get_password_length()
    password = generate_password(length)
    print(f"\nGenerated password: {password}")