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
        
    
def valid_data(get_data,check_data):
    for i in range(3):
        data = check_data(get_data())
        if data is not None:
            return data
    return None

def main():
    name = valid_data(get_name, check_name)
    age = valid_data(get_age, check_age)
    if name is not None and age is not None:
        print(f"Hello, {name}. You are {age} years old.")
    else:
        print('Game over')

main()