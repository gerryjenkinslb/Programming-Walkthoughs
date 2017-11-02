# name: Gerry Jenkins
# email: gerry.jenkins@gmail.com
# program: rock paper scissors

# version using basic program structure

import random

prompt = "Enter your choice:\nR or r for rock\nP or p for paper\nS or s for scissors\nQ or q to quit\n"

while True: # infinite loop till break
    user = input(prompt).lower() # lower case users input

    if user == 'q':
        break

    win = "you win against the comptuer"
    lose = "you lose against the comptuer"
    result = lose # default if not won

    comp = random.choice( ["rock", "paper", "scissors"] )
    print( "Computer picked:", comp)

    if comp[0] == user: # tie
        result = "you tie against the computer"
    else: # win or lose if structure
        if user == 'r':
            if comp == 'scissors':
                result = win
        if user == 'p':
            if comp == 'rock':
                result = win
        if user == 's':
            if comp == 'paper':
                result = win
    print(result)


