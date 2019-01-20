#!/usr/bin/env python
#This is a guess the number game.
import random


def main():
    secretNumber=random.randint(1,20)
    print('I am thinking of a number betdween 1 and 20.')

    #Ask the player to guess 6 times
    for guessesTaken in range(1,7):
        print('Take a Guess')
        guess=int(input())

        if guess < secretNumber:
            print('Your guees is too low.')

        elif guess > secretNumber:
            print('your guess is too high.')
            
            
        else:
            break # this condition is the correct guess!

    if guess==secretNumber:
        print('Good job! Your guessed my number in ' + str(guessestaken) + ' guesses!')
        
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))
        
    
        
        





if __name__ == '__main__':
    main()
