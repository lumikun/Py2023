# Uzrakstīt programmu teksta pārveidošanai
import re

try:
    txt = str(input("Please input a string: "))
    pass
except ValueError:
    print("Err... Input invalid!")
    exit()

print(re.sub("nav.*slikts", "ir labs", txt, 1))



