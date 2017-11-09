# name: Gerry Jenkins
# youtube channel: https://youtube.com/gjenkinslbcc
# program: rock paper scissors

# version using basic program after refactors
# also using python  s.format() template function
# use boolean expression in main if

import random

prompt = 'Enter your choice:\nR or r for rock\nP or p for paper\nS or s for scissors\nQ or q to quit\n'
out_template = 'you {} against the computer'

while True: # infinite loop till break
    user = input(prompt).lower() # lower case users input
    if user == 'q':
        break

    result = 'lose' # default if not won

    comp = random.choice( ['rock', 'paper', 'scissors'] )
    print( 'Computer picked:', comp)

    if comp[0] == user: # moved tie out of main if
        result = 'tie'
    else: # test if win
        if user == 'r' and comp == 'scissors':
                result = 'win'
        if user == 'p' and comp == 'rock':
                result = 'win'
        if user == 's' and comp == 'paper':
                result = 'win'
#    NOTE: above three if's can become one boolean expressions, just or the if expressions together
 
    print(out_template.format(result))


