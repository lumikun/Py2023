# 1. Lielais rezultāts
def add_multi(a: int, b: int, c: int) -> int:
    lst = [a, b, c]
    lst.sort()
    return (lst[0]+lst[1])*lst[2]

def input_num(usr_txt: str) -> int:
    try:
        ret = int(input(usr_txt))
        pass
    except ValueError as e:
        print("Err...")
        print(e)
        exit()
    return ret

x = input_num("Please input the 1st number: ")
y = input_num("Please input the 2nd number: ")
z = input_num("Please input the 3rd number: ")
print(add_multi(x, y, z))