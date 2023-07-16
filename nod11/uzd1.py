# 1. Reizinajums summa
# TODO 1.c
from functools import reduce


def sum_prod(s1, s2):
    return sum([reduce(lambda a, b: a*b, s1), reduce(lambda a, b: a*b, s2)])


def main():
    print(sum_prod((4, 5), [5, 2]))
    print(sum_prod([2, 3], [5, 10, 2]))


if __name__ == "__main__":
    main()
