import random

random_number = random.randint(1,10)

print("\n\nWelcome to \"Guess the number?\" Game!")
print("\nI'm thinking in a number between 1 and 10.")
print("\nCould you tell me which number is?")

times = 0
repeat = "y"

while repeat == "y":

    while times < 5:

        times += 1
        try:
            guessing = int(input("\nWhich number do you think it is?: "))
        except ValueError:
            guessing = 11
            print("\nError: Invalid input!")

        if guessing == random_number:
            print("\nYour guess is TRUE! Congrats!")
            break
        else:
            diff = guessing - random_number
            if abs(diff) == 1:
                print("\nFail! Hot! Try again!")
            elif abs(diff) == 2:
                print("\nFail! Warm! Try again!")
            elif abs(diff) == 3:
                print("\nFail! Warming up! Try again!")
            else:
                print("\nFail! You're cold! Try again!")
        
        print("\nYou have {0} tries left! Keep goin'!".format(5-times))

    repeat = input("\nDo you want to play again? [Yes/No]: ")
    repeat = repeat.lower()

    if repeat == "y" or repeat == "yes":
        times = 0
        continue
    else:
        break

print("\nThanks for playing!\n")