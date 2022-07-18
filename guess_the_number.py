import random

random_number = random.randint(1,10)

print("\n\nWelcome to \"Guess the number?\" Game!")

times = 0
repeat = "y"

while repeat == "y":

    print("\nPlease choose a Game Level:")
    print("1. Easy.")
    print("2. Challenging.")
    print("3. Mastermind.")
    level = input("\nWich level will you pick?: ")

    if level == "1":
        try_limit = 5
        random_number = random.randint(1,10)
        print("\nI'm thinking in a number between 1 and 10. You have 5 tries!")
    elif level == "2":
        try_limit = 5
        random_number = random.randint(1,20)
        print("\nI'm thinking in a number between 1 and 20. You have 5 tries!")
    elif level == "3":
        try_limit = 4
        random_number = random.randint(1,30)
        print("\nI'm thinking in a number between 1 and 30. You have 4 tries!")
    else:
        print("\nError: Invalid option. Please try again!")
        continue
    
    #print("\nCould you tell me which number is?")

    while times < try_limit:

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
        
        print("\nYou have {0} tries left! Keep goin'!".format(try_limit - times))

    repeat = input("\nDo you want to play again? [Yes/No]: ")
    repeat = repeat.lower()

    if repeat == "y" or repeat == "yes":
        times = 0
        continue
    else:
        break

print("\nThanks for playing!\n")