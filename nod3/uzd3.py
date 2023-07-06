# 3. Noprasiet lietotājam ievadīt 3 skaitļus, izvadiet tos sakārtotā secībā.
nums = []
for i in range(0, 3):
    try:
        n = float(input("Please enter a number: "))
        nums.append(n)
        pass
    except ValueError:
        print("Err... Not a valid input!")
        exit()

n = len(nums)
for i in range(n):
    sorted = True
    for j in range(n-i-1):
        if (nums[j] > nums[j+1]):
            nums[j], nums[j+1] = nums[j+1], nums[j]
            sorted = False
    if sorted:
        break

for i in range(3):
    print(nums[i])


