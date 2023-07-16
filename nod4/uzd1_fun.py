# fizzbuzz but functional style

def fizzbuzz(lst):
    b = list(filter(lambda a: a % 3 and not a % 5, lst))
    n = list(filter(lambda a: a % 3 and a % 5, lst))
    f = list(filter(lambda a: not a % 3 and a % 5, lst))
    fb = list(filter(lambda a: not a % 3 and not a % 5, lst))
    return (f, fb, b, n)


l = range(1, 101)
print(fizzbuzz(l))
