# 3. Apgrieztie vārdi
try:
    txt = str(input("Please input a sentence: "))
    txt = txt.lower().split()
    if not txt:
        raise ValueError
    pass
except ValueError as e:
    print("Err...")
    print(e)
    exit()

ans = ""

for word in txt:
    ans += word[::-1] + " "

print(ans.capitalize())