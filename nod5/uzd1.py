# Juceklis
try:
    txt = str(input("Please input a name: "))
    txt = txt[::-1].lower().capitalize()
    if not txt:
        raise ValueError
    pass
except ValueError as e:
    print("Err... \n ", e)
    exit()

print(f"{txt}, pamatigs juceklis vai ne {txt[-1].upper()}?")