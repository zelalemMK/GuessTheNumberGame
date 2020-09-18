#Guess the number 
#GODSPEED
from random import randint

name = input("What is your name? \n")
print("Well, " + name + ", I am thinking of a number between 1 and 20")

number = randint(1,21)
for gs in range(1,7):
    guess = int(input("Guess the number: "))
    if number == guess:
        print("Correct. The number was " + str(number))
        print("You took "+ str(gs) + " many guesses!")
        break
    elif number > guess:
        print("Too low.")
        print("Try again.")
    elif number < guess:
        print("Too High.")
        print("Try Again.")
if number != guess:
    print("You dumb ahh. its not that hard.")
