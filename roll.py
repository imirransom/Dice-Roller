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

def dice(roll_dice):
    if roll_dice == 1:
        print(f"Here is your dice roll: {random_number1}")
    elif roll_dice == 2:
        print(f"Here's")
