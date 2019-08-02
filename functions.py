def ask_name():
    print("Hello there, Whats you're name?")
    name = str(input())
    return name


def ask_age(name):
    print(f"Hello {name}, How old are you?")
    age = int(input())
    if age >= 18:
        return f"""{name} you're old enough to drink!!!"""
    else:
        return f"""Sorry {name}, you're too young to drink"""


def ask_questions():
    my_name = ask_name()
    return ask_age(my_name)


print(ask_questions())
