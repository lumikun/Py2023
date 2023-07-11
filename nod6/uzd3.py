# 3. Apgrieztie vārdi
try:
    txt = str(input("Please input a sentence: "))
    if not txt:
        raise ValueError
    pass
except ValueError as e:
    print("Err...")
    print(e)
    exit()

print(f"Your Sentence has been reversed: {txt[::-1].lower().capitalize()}")