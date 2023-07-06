# 2. Eglīte
def print_tree(h: int):
    for i in range(1, h+1):
        for j in range(h-i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()

try:
    h = int(input("Please input the tree's height: "))
    pass
except ValueError:
    print("Err... Invalid input!")
    exit()
print_tree(h)

