# 3. Pilsēta

p0 = 1000   # Current city population
perc = 2    # % value 0-100
delta = 50  # Delta, yearly imigration/emigration
p = 1200    # goal population

def get_city_year(p0: int, prct: int, d: int, p1: int) -> int:
    normalize = 0.01*prct
    #print(normalize)
    i = 0
    while (p0 <= p1):
        p0 = p0 + p0 * normalize + d
        i += 1
        if (p0 < 0):
            return -1
    return i

print(get_city_year(p0, perc, delta, p))
print(get_city_year(1000, 2, -50, 5000))
print(get_city_year(1500, 5, 100, 5000))
print(get_city_year(1500000, 2.5, 10000, 2000000))
