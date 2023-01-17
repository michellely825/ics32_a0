# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Michelle Ly
# lym8@uci.edu
# 62717883


def downward_block(user_input):
    first = "+-+"
    second = "| |"
    third = "+-+-+"
    indent = "  "
    for i in range(user_input):
        if i == 0:
            print(first)
            print(second)
            print(third)
        elif i == (user_input - 1):
            print(f'{indent * i}{second}')
            print(f'{indent * i}{first}')
        else:
            print(f'{indent * i}{second}')
            print(f'{indent * i}{third}')


user_input = int(input())
downward_block(user_input)
