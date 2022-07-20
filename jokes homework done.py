print('What do you get when you cross a snowman with a vampire?')
answer = input()

if answer.lower() == 'frostbite' or answer == 'Frostbite!':
    print(answer + ' is correct!')

else:
    print('Incorrect, the answer is not ' + answer + ' , take another guess.')
    print('What do you get when you cross a snowman with a vampire?')
    answer = input()
    if answer.lower() == 'frostbite' or answer == 'Frostbite!':
        print(answer + ' is correct!')

    else:
        print('Incorrect, the answer is frostbite!')
       

print('What do dentists call an astronaut\'s cavity')
answer = input()

if answer.lower() == 'a black hole' or answer.upper() == 'A BLACK HOLE!':
    print(answer + ' is correct!')

else:
    print('Incorrect, the answer is not ' + answer + ' , take another guess.')
    print('What do dentists call an astronaut\'s cavity')
    answer = input()
    if answer.lower() == 'a black hole' or answer.upper() == 'A BLACK HOLE!':
        print(answer + ' is correct!')

    else:
        print('Incorrect, the answer is a black hole!')

print('Here is another joke.')


answer = input('Knock, knock!\n')
 
if answer.lower() == "who's there?" or answer == "Who's there?" or answer == "who's there" or answer == "Who's there?":
    print('Interrupting cow!')
    answer = input()
    answer = str(answer)
    
    if answer.lower() == 'interrupting cow who?' or answer.upper() == 'INTERRUPTING COW WHO?' or answer == 'interrupting cow who':
        print('Moooooo')
        input()
        print(end='Thats the end of my comedy career.')
            
    else:
        print('You typed ' + answer + ' .Please type "interrupting cow who?" to continue.')
        input('mooo\n')
        answer = input('Moooo\n')
        print(end='Thats the end of my comedy career.')
else:
    print('You typed ' + answer + ' .Please type, "Who\'s there?"')

    print(end='Thats the end of my comedy career.')
