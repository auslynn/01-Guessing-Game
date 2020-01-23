import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

import random

guessesTaken = 0
guessesLeft = 20

number = random.randint(1,50)

while guessesTaken < 20:
    guessesLeft = str(guessesLeft)
    print("I'm guessing of an integer between 1 and 50. Can you guess what it is? You have " +guessesLeft + " guesses left.")
    print()
    guess = input()
    guessesLeft = int(guessesLeft)

    guessesTaken = 1 + guessesTaken
    guessesLeft = guessesLeft - 1

    if not guess.isdigit():
        print("That's not an integer! Follow the rules, guess a number between 1 and 50.")
        print()

    elif int(guess) < 1 or int(guess) > 50:

        if int(guess) == 69 or int(guess) == -69:
            print ("Haha, very funny. Try again with a number between 1 and 50.")
            print()

        elif int(guess) == 420 or int(guess) == -420:
            print ("Very mature. Try again with a number between 1 and 50.")
            print()

        elif int(guess) == 62:
            print ("That's my favorite number! But it's not between 1 and 50, so try again.")

        else:
            print("That's outside of the scope of this game! Follow the rules, guess a number between 1 and 50.")
            print()

    else:

        if int(guess) > number:
            print("Sorry, your guess was too high. Try again.")
            print()

        if  int(guess) < number:
            print("Sorry, your guess was too low. Try again.")
            print()

        if int(guess) == number:
            break

if int(guess) == number:
    guessesTaken = str(guessesTaken)
    guessesLeft = str(guessesLeft)
    number = str(number)
    print("Nice job, you guessed the number I was thinking of, " +number+ ", in " +guessesTaken+ " turns!")
    print()
    print("You finished with " +guessesLeft+ " guesses left. Re-run the program to play again!")
    print()

elif int(guess) != number:
    guessesTaken = str(guessesTaken)
    guessesLeft = str(guessesLeft)
    number = str(number)
    print("Sorry, you didn't guess my number in 20 turns. The number I was thinking of was " +number+ ".") 
    print("Run the program again to try again!")
    print()
    