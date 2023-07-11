# Uzrakstīt programmu teksta simbola atpazīšanai ??? STUB
from getpass import getpass

txt = getpass("Please input a string to guess: ")

print("Please take a guess: "+"*"*len(txt))

guesses = ''

turns = 20

while turns > 0:
    failed = 0
    for char in txt:
        if char in guesses:
            print(char, end = "")
        else: 
            print("*", end="")
            failed += 1
    if failed == 0:
        print("You Win")

        print("The word is: ", txt)
        break
    print()
    guess = input("Guess a Char: ")
    guesses += guess
    if guess not in txt:
        turns -= 1
        print("Wrong")
        print(f"You have {turns} left!")
        if turns == 0:
            print("You Lost")