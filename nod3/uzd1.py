# Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.

try:
    temp = float(input("What's your body temperature? "))
    pass
except ValueError:
    print("Err... Please input a valid Temperature value!!!")
    exit()

if (temp < 35):
    print("Looks like you might be cold?")
elif (temp >= 35 and temp <= 37):
    print("You look healthy!")
else:
    print("You might have a fever!!!")