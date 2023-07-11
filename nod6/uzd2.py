# 2. Kubu tabula

def input_num(usr_txt: str) -> int:
    try:
        ret = int(input(usr_txt))
        pass
    except ValueError as e:
        print("Err...")
        print(e)
        exit()
    return ret


low_bound = input_num("Please input the lower bound of the list: ")
upper_bound = input_num("Please input the upper bound of the list: ") + 1
lst = [*range(low_bound, upper_bound, 1)]
sqr_lst = []
for i in lst:
    print(f"{i} cubed: {i**3}")
    sqr_lst.append(i**3)

print(f"All cubed: {sqr_lst}")