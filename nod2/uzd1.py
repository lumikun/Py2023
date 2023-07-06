import datetime

name = input("What's your name? ")
if not name:
    print("Err...")
    print("Input name!!!")
    exit()
current_year = datetime.datetime.now().year
age = int(input(f"Hi, {name}! How old are you? "))
century_old = (current_year - age) + 100
print(f"So you're {age} years old, that would mean you turn 100, years old in {century_old}")
