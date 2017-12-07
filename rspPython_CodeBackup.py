###
#   Rock, Paper, Scissors!
###
#   Version: Python 2.7.13
#
#   Author: Josh Batchelor, 12/5/2017
#
#   Purpose: Make a simple RPS game.
#

import time
import random
import math

moves = ['rock','paper','scissors']
cp = "Computer "
pl = "Human "
pPts = 0
cPts = 0


print("Rock, Paper Scissors game. You vs. {}".format(cp))
print("NOTE: Only enter rock, paper, or scissors as a move!")
print("Best 2 out of 3 wins.")
print("Round 1!")


while True:
    if pPts == 3 or cPts == 3:
        break
    pm = raw_input("What's your move? ").lower()
    if pm == moves[0] or pm == moves[1] or pm == moves[2]:
        print("You chose " + pm + ".")
            
    cm = random.choice(moves)
    print(cp + " chose " + cm + ".")
    
    if cm == pm:
        print("It's a draw!")
        


    if cm == moves[0] and pm == moves[1]:
        pPts = pPts + 1
        print(pl + "won. " + pl + "has " + str(pPts) + " points.")
        

    if cm == moves[0] and pm == moves[2]:
        cPts = cPts + 1
        print(cp + "won. " + cp + "has " + str(cPts) + " points.")
        
        

    if cm == moves[1] and pm == moves[0]:
        cPts = cPts + 1
        print(cp + "won. " + cp + "has " + str(cPts) + " points.")
        

    if cm == moves[1] and pm == moves[2]:
        pPts = pPts + 1
        print(pl + "won. " + pl + "has " + str(pPts) + " points.")
        



    if cm == moves[2] and pm == moves[0]:
        pPts = pPts + 1
        print(pl + "won. " + pl + "has " + str(pPts) + " points.")
        

    if cm == moves[2] and pm == moves[1]:
        cPts = cPts + 1
        print(cp + "won. " + cp + "has " + str(cPts) + " points.")
        

    if pPts == 3 or cPts == 3:
        break

print("*GAME HAS ENDED*")
if pPts > cPts:
    print("You are the winner!")
else:
    print(cp + "is the winner!") 
print("Goodbye")
