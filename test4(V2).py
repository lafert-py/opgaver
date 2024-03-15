import re


def get_name():
    name = input("What is your name? ").split()
    name = [element.capitalize() for element in name]

    return name


def get_age():
    age = input("What is your age? ")
    return age


def check_name(name):

    # Allowed symbols . or -
    symbols = [
        "+",
        "*",
        "/",
        "=",
        "<",
        ">",
        "^",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "<",
        ">",
        ",",
        ";",
        ":",
        '"',
        "'",
        "?",
        "!",
        "@",
        "#",
        "$",
        "%",
        "&",
        "_",
        "\\",
        "|",
        "~",
        "`",
        "^",
    ]

    try:
        for word in name:
            if re.search(r"\d", word):
                raise ValueError("The name contains numbers")

            elif any(elem in symbols for elem in word):
                raise ValueError("The name contains special symbol")

        return " ".join(name)
    except ValueError as e:
        print(e)


def check_age(age):
    try:
        if age.isdigit():
            age = int(age)
            if age > 100:
                raise ValueError("You are not human :-)")

            else:
                return age
        else:
            raise ValueError("The value is wrong. You need to enter numbers.")

    except ValueError as e:
        print(e)


def valid_data(get_data, check_data):
    for i in range(3):
        data = check_data(get_data())
        if data is not None:
            return data
    print("Game over")
    return None


def main():
    name = valid_data(get_name, check_name)
    if name is None:
        return

    age = valid_data(get_age, check_age)
    if name is None:
        return

    print(f"Hello, {name}. You are {age} years old.")


main()
