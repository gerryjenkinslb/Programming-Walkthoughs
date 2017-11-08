# name: Gerry Jenkins
# email: gerry.jenkins@gmail.com
# program: rock paper scissors

# version using 'lookup table' program structure

import random

prompt = "Enter your choice:\nR or r for rock\nP or p for paper\nS or s for scissors\nQ or q to quit\n"

# dictionary with entries to lookup result


# lookup win or lose
rules = { 'rr':'tie',  'rp':'lose', 'rs':'win',
          'pr':'win',  'pp':'tie',  'ps':'lose',
          'sr':'lose', 'sp':'win',  'ss':'tie' }

# lookup full name form letter
full_names = { 'r':'Rock', 'p':'Paper', 's':'Scissors' }

while True: # infinite loop till break
    user = input(prompt).lower() # lower case users input

    if user == 'q':
        break

    comp = random.choice( 'rps') # pick singe char

    print('Computer picked: ', full_names[comp])
    print('you', rules[user + comp], 'against the computer')







