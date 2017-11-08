# complete lookup table

import random

dtble = { 
    'rs':'win', 'pr':'win', 'sp':'win', 
    'sr':'lose', 'rp':'lose', 'ps':'lose', 
    'rr':'tie', 'pp':'tie', 'ss':'tie' }

while True: # infinite loop till break
    print("Enter your choice:\nR or r for rock\nP or p for paper\nS or s for scissors\nQ or q to quit\n")
    user = input().lower() # lower case users input
    if user == 'q': break

    comp = random.choice( ['Rock', 'Paper', 'Scissors'])
    print('Computer Picked:', comp)

    # format template, lookup win lose tie, and ouput
    print("You {} against the computer".format(dtble[user+comp[0].lower()]))
