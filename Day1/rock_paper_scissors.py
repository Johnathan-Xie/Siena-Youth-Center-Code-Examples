import argparse
import random
def play(player_choice, computer_choice):
    if (player_choice == computer_choice):
        print('Computer played ' + computer_choice + ". It's a tie.")
    
    elif (player_choice == 'rock'):
        if(computer_choice == 'scissors'):
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

#for students to complete
def play_win(player_choice):
    if player_choice == 'scissors':
        return 'rock'
    if player_choice == 'paper':
        return 'scissors'
    if player_choice == 'rock':
        return 'paper'
    else:
        raise ValueError
    #winning_values = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}
    #return winning_values[player_choice]

if __name__ == '__main__':
    inp = input()
    while inp != "":
        #play(inp, random.choice(['rock', 'paper', 'scissors']))
        play(inp, play_win(inp))
        inp = input()