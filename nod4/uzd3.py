# 3. Pirmskaitlis
from math import isqrt

def is_prime(n: int) -> bool:
    if (n <= 3):
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (n+1) == 0:
            return False
    return True

try:
    n = int(input("Please enter a number: "))
    pass
except ValueError:
    print("Err... Invalid input!")
    exit()

if (is_prime(n)):
    print(f"The number {n} is a prime number!")
else:
    print(f"The number {n} is not a prime number!")

