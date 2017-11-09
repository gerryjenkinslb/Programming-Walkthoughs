# name: Gerry Jenkins
# youtube channel: https://youtube.com/gjenkinslbcc
# program: rock paper scissors

# version using basic program structure, NOTE a lot of redundant code

import random

prompt = 'Enter your choice:\nR or r for rock\nP or p for paper\nS or s for scissors\nQ or q to quit\n'

while True: # infinite loop till break
    user = input(prompt).lower() # lower case users input

    if user == 'q':
        break # exit program

    comp = random.choice( ['rock', 'paper', 'scissors'] ) # random pick
    print( 'Computer picked:', comp)

    if user == 'r':
        if comp == 'rock':
            print('you tie against the computer')
        if comp == 'paper':
            print('you lose against the computer')
        if comp == 'scissors':
            print('you win against the computer')
            
    if user == 'p':
        if comp == 'rock':
            print('you win against the computer')
        if comp == 'paper':
            print('you tie against the computer')
        if comp == 'scissors':
            print('you lose against the computer')
            
    if user == 's':
        if comp == 'rock':
            print('you lose against the computer')
        if comp == 'paper':
            print('you win against the computer')
        if comp == 'tie':
            print('you win against the computer')


