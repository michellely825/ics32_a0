# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Michelle Ly
# lym8@uci.edu
# 62717883

def downwardBlock(userInput):
    first = "+-+"
    second = "| |"
    third = "+-+-+"
    indent = "  "
    for i in range(userInput): #0 to userInput - 1
        if i == 0:
            print(first)
            print(second)
            print(third)
        elif i == (userInput - 1):
            print(f'{indent * i}{second}')
            print(f'{indent * i}{first}')
        else:
            print(f'{indent * i}{second}')
            print(f'{indent * i}{third}')

userInput = int(input())
downwardBlock(userInput)
