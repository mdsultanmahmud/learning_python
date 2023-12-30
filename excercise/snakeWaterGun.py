"""
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. 
Write a python program to create a snake water gun game in python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win. 
"""

import random 

user = int(input("Chose anything between Snake, Water and Gun:\n 0 for Snake \n 1 for Water and \n2 for Gun \n==: "))

computer = random.randint(0, 2) 

print(computer, user)
def check(computer, user):
    if computer == user:
        return 0
    if (computer == 0 and user == 1):
        return -1 
    if (computer == 1 and user == 2):
        return -1 
    if (computer == 2 and user == 0):
        return -1 
    return 1 
score = check(computer, user)
if(score == 0):
    print("Game is Draw!!")
elif (score == 1):
    print("You Win!! Enjoy the moment!!!")
else:
    print("You Lose! Enjoy the moment!!!")
  

    