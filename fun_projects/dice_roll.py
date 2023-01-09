# program that simulates rolling of a dice in the terminal

import random

dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

}

# function to roll the dice
def rollDice():
    # initiate the roll
    roll = input("Do you want to roll the dice? (yes/no): ")
    
    while roll.lower() == 'yes':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        print("dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))        
        roll = input("Roll again? (yes/no): ")

# activate dice roll        
rollDice()