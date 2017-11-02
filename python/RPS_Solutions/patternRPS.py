# name: Gerry Jenkins
# email: gerry.jenkins@gmail.com
# program: rock paper scissors

# version using 'pattern string' program structure

import random

prompt = "Enter your choice:\nR or r for rock\nP or p for paper\nS or s for scissors\nQ or q to quit\n"


wins = "rs pr sp" # these are the only wins, look up 2 char user/comp

while True: # infinite loop till break
    user = input(prompt).lower() # lower case users input

    if user == 'q':break

    comp = random.choice( ['Rock', 'Paper', 'Scissors'])
    print('Computer Picked:', comp)

    comp_char = comp[0].lower()
    fs = "You %s against the computer"

    if (user + comp_char) in wins:
        print( fs % ('win'))
    elif user == comp_char:
        print( fs % ('tie'))
    else:
        print( fs % ('lose'))



