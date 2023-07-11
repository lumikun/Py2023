# 4. Pirmskaitļi - šis varētu būt nedēļas nogales uzdevums, klasē diez vai pietiks laika
def input_num(usr_txt: str) -> int:
    try:
        ret = int(input(usr_txt))
        pass
    except ValueError as e:
        print("Err...")
        print(e)
        exit()
    return ret

def sieve(bound: int):
    prime = [True for i in range(bound+1)]

    p = 2
    while (p * p <= bound):
        if (prime[p] == True): 
            for i in range(p*p, bound+1, p):
                prime[i] = False
        p += 1
    for p in range(2, bound+1):
        if prime[p]:
            print(p)

upper_bound = input_num("Please input the upper bound for Prime sieve: ")
print(f"These are all the primes up to {upper_bound}!")
sieve(upper_bound)