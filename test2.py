def get_name():
    name = input("What is your name? ").split()
    name = [element.capitalize() for element in name]
    # name = " ".join(name)
    return name


def get_age():
    age = input("What is your age? ")
    return age


def check_name(name):
    test = all(element.isalpha() for element in name)
    if test:
        return " ".join(name)

    else:
        print("The value is wrong. You need to enter letters.")
        return None


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
        return None


def quantity_probes():
    for i in range(3):
        name = check_name(get_name())
        if name is not None:
            break
    if name is None:
        return None, None
    for i in range(3):
        age = check_age(get_age())
        if age is not None:
            break
    if age is None:
        return None, None
    return name, age


def main():
    name, age = quantity_probes()
    if name is not None and age is not None:
        print(f"Hello, {name}. You are {age} years old.")
    else:
        print("Game over")


main()
