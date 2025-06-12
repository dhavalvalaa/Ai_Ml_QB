# Develop a number guessing game where the program selects a random number, and
# the user tries to guess it within a limited number of attempts.

import random as rn

def game():
    bn = rn.randint(1,11)

    for i in range(1,4):
        print(f"try number {i}")
        n = int(input("guess the number(1,10) = "))

        if n == bn:
            print("done")
            break

        else:
            if n > bn:
                print("number is higher! try again!\n")
            else:
                print("number is lower! try agian !\n")
            
game()