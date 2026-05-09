def get_user_input():
    name = input("Enter your name: ").strip()
    age = input("Enter your age: ").strip()
    return name, age


def validate_age(age: str) -> int:
    if not age.isdigit():
        raise ValueError("Age must be a positive integer.")
    age_int = int(age)
    if not (0 < age_int < 150):
        raise ValueError("Age must be between 1 and 149.")
    return age_int


def format_greeting(name: str, age: int) -> str:
    if not name:
        raise ValueError("Name cannot be empty.")
    if age < 10:
        age_group = "a single-digit superstar"
    else:
        decade = (age // 10) * 10
        age_group = f"a proud member of the {decade}s club"
    return (
        f"Hello, {name}! 👋\n"
        f"You are {age} years old — {age_group}!"
    )


def main():
    name, raw_age = get_user_input()
    age = validate_age(raw_age)
    print(format_greeting(name, age))


if __name__ == "__main__":
    main()