# This is a Guess the Number game. TESTER CODE
import random

guessTaken = 0
print('Hello, welcome to Waynes guess the number game, What is your name?')
myName = input()
print('Nice to meet you, ' + myName + ' lets get started.')
for guessesTaken in range(100):


    print('Lets play guess the number game. Choose your difficulty, easy, medium, hard or extreme.')
    difficulty = input()
    difficulty = str(difficulty)
    print('I see that you have chosen ' + difficulty)
        
    if difficulty == 'easy':
            number = random.randint(1, 10)
            print('Well, ' + myName + ', I am thinking of a number between 1 and 10. You get 3 guesses')
            print('Take a guess.') # Four spaces in front of "print".
            for guessesTaken in range(3):
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
            print('Well, ' + myName + ', I am thinking of a number between 1 and 20. You get 4 guesses')
            print('Take a guess.') # Four spaces in front of "print".
            for guessesTaken in range(4):
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
            print('Well, ' + myName + ', I am thinking of a number between 1 and 30. You get 5 guesses')
            print('Take a guess.') # Four spaces in front of "print".
            for guessesTaken in range(5):
                guess = input()
                guess = int(guess)

                if guess < number:
                    print('Your guess is too low.') # Eight spaces in front of "print"

                if guess > number:
                    print('Your guess is too high.')

                if guess == number:
                    break

    if difficulty == 'extreme':
            number = random.randint(1, 550)
            print('Well, ' + myName + ', I am thinking of a number between 1 and 550. Only a few users have guessed my number in extreme mode. You get 10 guesses. Good luck.')
            print('Take a guess, if you dare.') # Four spaces in front of "print".
            for guessesTaken in range(10):
                guess = input()
                guess = int(guess)

                if guess < number:
                    print('Your guess is too low.') # Eight spaces in front of "print"

                if guess > number:
                    print('Your guess is too high.')

                if guess == number:
                    break

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number + '.')
