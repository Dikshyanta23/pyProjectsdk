# create a program to simulate a game of rock, paper, scissor between the user and the computer
import random
def main():
    # loop the game until the user desires to quit
    status = True
    while (status):
        user_input = input("Please enter r for rock, p for paper,s for scissors and q for quit: ")
        user_input_lower = user_input.lower()
        # generating computer choices
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        # for rock
        if user_input_lower == 'r':
            if computer_choice == 'rock':
                print('Computer: rock\nIts a draw\n')
            elif computer_choice == 'scissors':
                print('Computer: scissors\nYou win.\n')
            else:
                print('Computer: paper\nYou lose.\n')
        # for scissors
        elif user_input_lower == 's':
            if computer_choice == 'rock':
                print('Computer: rock\nYou lose\n')
            elif computer_choice == 'scissors':
                print('Computer: scissors\nIts a draw.\n')
            else:
                print('Computer: paper\nYou win.\n')
        # for paper
        elif user_input_lower == 'p':
            if computer_choice == 'rock':
                print('Computer: rock\nYou win\n')
            elif computer_choice == 'scissors':
                print('Computer: scissors\nYou lose.\n')
            else:
                print('Computer: paper\nIts a draw.\n')
        # for quit
        else:
            print('Thank you')
            status = False
    
#execute main       
main()