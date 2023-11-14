import random

# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#

random_number1 = random.randint(1, 7)
random_number2 = random.randint(1, 7)
random_number3 = random.randint(1, 7)
random_number4 = random.randint(1, 7)

def user_input():
    return input("Please choose how many times you would like to roll the dice:\n1.\n2.\n3.\n")

def dice():
    user_input()
    roll_dice = user_input()
    while True:
        if roll_dice == "1":
            print(f"Here is your dice roll: {random_number1}")
            break
        elif roll_dice == "2":
            print(f"Here's you first roll: {random_number1}\nAnd your second roll: {random_number2}")
            break
        elif roll_dice == '3':
            print(f"Your first roll: {random_number1}\nSecond Roll: {random_number2}\nThird Roll: {random_number3}")
            break
        else:
            print("Wrong selection, please choose how many times you want to roll the dice.")
            continue

dice()

