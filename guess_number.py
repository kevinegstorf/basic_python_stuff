# This is a Guess the Number Game.
import random

print('Hello what is your name?')

player = input()
playerName = player.capitalize()

print('Well, ' + playerName + ', I am thinking of a number between one and twenty.')
print('Can you guess what it is?')

secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #this condition is for the correct guess

if guess == secretNumber:
    print(playerName + ' you must be a mindreader it only took you ' + str(guessesTaken) +' guesses, great job!')
else:
    print('Bummer ' + playerName + ' the number i was thinking of was ' + str(secretNumber) )
