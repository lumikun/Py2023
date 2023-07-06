#  1. FizzBuzz
try:
    n = int(input("Please input the bound for FizzBuzz: "))
    pass
except ValueError:
    print("Err... Invaldi input.")
    exit()

for i in range(1, n):
    if (i % 3 == 0):
        if (i % 5 == 0):
            print("FizzBuzz")
        print("Fizz")
    if (i % 5 == 0):
        print("Buzz")
    print(i)
