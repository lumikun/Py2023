# Uzrakstīt programmu teksta pārveidošanai 
import re

try:
    txt = str(input("Please input a string: "))
    if not txt:
        raise ValueError
    pass
except ValueError as e:
    print("Err...")
    print(e)
    exit()

print(re.sub("nav.*slikts", "ir labs", txt, 1))



