# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.

num_list = []

def num_input():
    try:
        n = float(input("Please input a number: "))
        num_list.append(n)
        pass
    except ValueError as e:
        print("Err...")
        print(e)
        exit()

def average_list(lst) -> float:
    return sum(lst) / len(lst)

try:
    size = int(input("Please input the size of the list: "))
    pass
except ValueError as e:
    print("Err...")
    print(e)
    exit()

for i in range(size):
    num_input()

num_list.sort()
avg = average_list(num_list)

print(f"The Top 3: {num_list[:3]}, The Bottom 3{num_list[-3:]}")
print(f"The average of the list is: {avg}")
