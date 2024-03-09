def get_name():
    for i in range(3):
        name = input("What is your name? ").split()

        test = all(element.isalpha() for element in name)

        if test:
            name = [element.capitalize() for element in name]
            name = " ".join(name)
            return name

        else:
            print("The value is wrong. You need to enter letters.")
    return None


def get_age():
    for i in range(3):
        age = input("What is your age? ")

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


def main():
    name = get_name()
    if name is None:
        return
    age = get_age()
    if age is None:
        return
    print(f"Hello, {name}. You are {age} years old.")


main()
