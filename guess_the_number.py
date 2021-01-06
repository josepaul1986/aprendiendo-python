import random

random_number = random.randint(1,10)

print("Welcome to \"Guess the number?\" Game!")
print("\nI'm thinking in a number between 1 and 10.")
print("\nCould you tell me which is?")

times = 0

while True:
    guessing = int(input("\nWhich number is?: "))

    times += 1

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

    if times == 5:
        repeat = input("\nDo you want to play again? [Yes/No]")
        repeat = repeat.lower()
        if repeat == "y" or repeat == "yes":
            random_number = random.randint(1,10)
            continue
        else:
            break

print("\nThanks for playing!\n")