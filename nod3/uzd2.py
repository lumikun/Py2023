# Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.

try:
    monthly_pay = float(input("What's your monthly wage? "))
    pass
except ValueError:
    print("Err... Please input a valid value!!!")
    exit()

try: 
    years = int(input("How many full years have you worked at the company? "))
    pass
except ValueError:
    print("Err... Please input a valid value!!!")
    exit()

if (years <= 2):
    print(f"Your Christmas bonus is going to be {monthly_pay*0.15}€.")
else:
    print(f"Looks like your Christmas bonus will be {monthly_pay*0.15*(years-2)}€.")

