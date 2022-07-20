# This is a Guess the Number game. HOMEWORK
import random

guessTaken = 0

##difficulty = 'easy'
##difficulty = 'medium'
##difficulty = 'hard'
print('Hello! What is your name?')
myName = input()
print('Nice to meet you, ' + myName + ' lets get started')


##number = random.randint(1, 20)
##print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

print('Lets play guess the number game. Choose your difficulty, easy, medium or hard.')
difficulty = input()
difficulty = str(difficulty)
print('I see that you have chosen ' + difficulty)
#for guessesTaken in range(6):
##    difficulty = input()
##    difficulty = str(difficulty)
##    print('I see that you have chosen ' + difficulty)


        
if difficulty == 'easy':
        number = random.randint(1, 10)
        print('Well, ' + myName + ', I am thinking of a number between 1 and 10.')
        print('Take a guess.') # Four spaces in front of "print".
        for guessesTaken in range(6):
            guess = input()
            guess = int(guess)

            if guess < number:
                print('Your guess is too low.') # Eight spaces in front of "print"

            if guess > number:
                print('Your guess is too high.')

            if guess == number:
                break

        
if difficulty == 'medium':
        number = random.randint(1, 20)
        print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
        print('Take a guess.') # Four spaces in front of "print".
        for guessesTaken in range(6):
            guess = input()
            guess = int(guess)

            if guess < number:
                print('Your guess is too low.') # Eight spaces in front of "print"

            if guess > number:
                print('Your guess is too high.')

            if guess == number:
                break


if difficulty == 'hard':
        number = random.randint(1, 30)
        print('Well, ' + myName + ', I am thinking of a number between 1 and 30.')
        print('Take a guess.') # Four spaces in front of "print".
        for guessesTaken in range(6):
            guess = input()
            guess = int(guess)

            if guess < number:
                print('Your guess is too low.') # Eight spaces in front of "print"

            if guess > number:
                print('Your guess is too high.')

            if guess == number:
                break

##        if guess < number:
##            print('Your guess is too low.') # Eight spaces in front of "print"
##
##        if guess > number:
##            print('Your guess is too high.')
##
##        if guess == number:
##        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
