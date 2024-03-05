def get_name():
    for i in range(3):
        name = input("What is your name? ")
        if name.isalpha():
            return name
        else:
            print("The value is wrong. You need to enter letters.")
    return None


def get_age():
    for i in range(3):
        age = input("What is your age?")
        try:
            age = int(age)
            return age

        except:
            print("The value is wrong. You need to enter nunbers.")
    return None


def main():
    name = get_name()
    if name is None:
        return
    age = get_age()
    if age is None:
        return
    print(f"Hello, {name.capitalize()}. You are {age} years old.")


main()
