import argparse
import random
def play(player_choice, computer_choice):
    if (player_choice == computer_choice):
        print('Computer played ' + computer_choice + ". It's a tie.")
    
    elif (player_choice == 'rock'):
        if(computer_choice == 'paper'):
            print('Computer plays scissors. You win!')
        else:
            print('Computer plays paper. You lose!')
    
    elif (player_choice == 'paper'):
        if(computer_choice == 'rock'):
            print('Computer plays rock. You win!')
        else:
            print('Computer plays scissors. You lose!')
    
    elif (player_choice == 'scissors'):
        if(computer_choice == 'paper'):
            print('Computer plays paper. You win!')
        else:
            print('Computer plays rock. You lose!')
    else:
        print('invalid choice')

if __name__ == '__main__':
    inp = input()
    while inp != "":
        play(inp, random.choice(['rock', 'paper', 'scissors']))
        inp = input()