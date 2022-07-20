import time
import random
"""World of Wallstreet 2022"""




def displayIntro():
    print('Welcome to the World of Wallstreet...')
    print('PRESS ENTER TO PLAY.')
    input()
    time.sleep(2)

    print('In America many people lie to your face and take your cash while you\'re confused...')
    print('\n')#creates space between print statements
    time.sleep(3)#sleeps for 5 seconds

    print('''America was not always like this, and neither was it\'s stock market.
Capitalism has birthed billionaires while condemning over 40% of the population to poverty...''')
    print('\n')
    time.sleep(3)

    print('''How could this happen to America? Once an honorable, safe, free and fair country,
America now has become a ghost of it\'s former self...''')
    print('\n')
    time.sleep(3)

    print('The rich get richer and the poor get poorer, that\'s what everyone says.')
    print('\n')
    time.sleep(3)

    print('What most folks don\'t realize is that the rich are getting richer by cheating, stealing and lying.')
    print('\n')
    time.sleep(3)

    print('''The poor will get locked away for committing a crime, or even be fined more than their weekly wage,
while the rich pay a fine that is 1% of their daily wage or they\'re not punished at all.''')
    print('\n')
    time.sleep(3)

    print('Press enter to continue.')
    input()
    time.sleep(3)
    print('\n')
    print('''This brings us to the stock market today, where the greatest financial schemes of our time
is formulated by accredited wall street investors, institutional investors, market makers, and other
fraudulent market participants. These individuals and groups of people don\'t want retail investors to
know how the market and it\'s laws actually work, so it\'s not surprising that most don't understand how one works, the
market are rigged, just like many other not-so-credible systems in America, this corruption is huge because
the stock market is at the center of US financial industry. Right now all you need to know is that if the stock market is
corrupted then everything is corrupted.''')
    print('\n')
    time.sleep(3)
    print('Before we go please choose the suit you would like to bring with you...')
    input()
    time.sleep(1)
    print('We have three to choose from, black, blue, red, or green.' )
    input()
    time.sleep(1)
    print('Please choose one...')

def data(userData):
    print(userData)
    print('press a for blue.')
    print('press b for black.')
    print('press c for red.')
    print('press d for green.')
    
    Answer = input()
    while Answer != 'a' or Answer != 'b' or Answer != 'c' or Answer != 'd':
        
        
        if Answer == 'a':
            userData['Suit'] = 'blue suit'
            
            return userData
            
        if Answer == 'b':
            userData['Suit'] = 'black suit'
            
            return userData
            
        if Answer == 'c':
            userData['Suit'] = 'red suit'
            
            return userData
            
        if Answer == 'd':
            userData['Suit'] = 'green suit'
            
            return userData
            
        else:
            print('Try that one more time.')
            print('press a for blue.')
            print('press b for black.')
            print('press c for red.')
            print('press d for green.')
            Answer = input()

            while Answer != 'a' or Answer != 'b' or Answer != 'c' or Answer != 'd':

            
                if Answer == 'a':
                    userData['Suit'] = 'blue suit'
                    
                    return userData
                    
                if Answer == 'b':
                    userData['Suit'] = 'black suit'
                    
                    return userData
                if Answer == 'c':
                    userData['Suit'] = 'red suit'
                    
                    return userData
                if Answer == 'd':
                    userData['Suit'] = 'green suit'
                    
                    return userData

                else:
                    break

def filler(userData):
    print(userData)
    print('One more thing before we begin, will you please tell me what type of trader you are?')
    print('\n')
    time.sleep(3)
    print('There are many types of traders in the world, but we are just going to focus on a few. Bull, bear, swing, value...')
    print('\n')
    time.sleep(2)
    print('''A bull or bullish trader focuses on ascending stocks over a mid-long period of time, sometimes
basing trades off of investor sentiment, good news about the company, technical and fundamental analysis.''')
    print('\n')
    time.sleep(2)
    print('''A bear or bearish trader is someone who bets that a stock is going to drop in price
by borrowing shares of the targeted stock to sell at a high price and buy it back at a lower price, eventually
return those shares to those who lent them while pocketing the difference. Its the opposite of investing, this can
be a short sell over one day to infinity if the short seller has big enough wallets.''')
    print('\n')
    time.sleep(2)
    print('''Swing traders simply place trades on technical analysis, historical action and fundamentals. These trades
can be for one day to about a month.''')
    print('\n')
    time.sleep(2)
    print('''Value investing is above all the cream of the crop. You notice good companies if you are good at investing,
if you see a need for a product that a good company has and you are willing to buy shares of that company because
simply put, you believe in that company and you think it\'s your lucky winner.''')
    print()
    
def data2(userData):
    print(userData)
    print('press a for bull.')
    print('press b for bear.')
    print('press c for swing.')
    print('press d for value.')
    Answer = input()

    while Answer != 'a' or Answer != 'b' or Answer != 'c' or Answer != 'd':

        if Answer == 'a':
            userData['Type of trader'] = 'bull'
            
            return userData
            
        if Answer == 'b':
            userData['Type of trader'] = 'bear'
            
            return userData
            
        if Answer == 'c':
            userData['Type of trader'] = 'swing'
            
            return userData

        if Answer == 'd':
            userData['Type of trader'] = 'value'
            
            return userData
               
        else:

            while Answer != 'a' or Answer != 'b' or Answer != 'c' or Answer != 'd':

                print('Thats not a valid entry, please select one of the following...')
                Answer = input()
                print(userData)
                print('press a for bull.')
                print('press b for bear.')
                print('press c for swing.')
                print('press d for value.')
                if Answer == 'a':
                    userData['Type of trader'] = 'Bull'
                    print(userData)

                    
                if Answer == 'b':
                    userData['Type of trader'] = 'Bear'
                    print(userData)
                    return userData
                    
                if Answer == 'c':
                    userData['Type of trader'] = 'Swing'
                    print(userData)
                    return userData

                if Answer == 'd':
                    userData['Type of trader'] = 'Value'
                    print(userData)
                    return userData

                else:
                    break

def frontDoor():
    time.sleep(3)
    print('Press enter to continue.')
    input()
    time.sleep(3)
    print('''We have kept you waiting long enough, we are sending you to one of the most
corrupted places on the planet, a stock exchange.''')
    print('\n')
    time.sleep(2)
    print('It\'s time to begin.')
    time.sleep(2)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('Press enter to wake up.')
    input()
    print('\n')
    print('''You wake up and find yourself in front of the NYSE, A.K.A. the
New York Stock Exchange.''')
    time.sleep(2)
    print('\n')
    print('Press enter to walk.')
    input()
    time.sleep(2)
    print('\n')
    print('''You walk up to the door, where a Bouncer greets you.
The bouncer stands 10 feet tall and is wearing a bullet proof vest under a tuxedo,
he has a weird smell to him, like burnt paper.''')
    print('\n')
    time.sleep(2)

    print('''Bouncer: Before you can come inside you have to guess the
secret number''')
    time.sleep(4)
    print()
          

def userName():
    
    print('''Bouncer: Before we begin, let\'s introduce ourselves,
my name is The Bouncer.''')
    time.sleep(2)
    print()
    print('Bouncer: Who are you? What\'s your name?')
    
    myName = input()
    
    return myName
    
    
def bouncer(myName):
    
    number = random.randint(1, 50)
    guessesTaken = 0
    print('Bouncer: It\'s good to meet you ' + myName + '...')
    print('Bouncer: Alright, lets get started, I am thinking of a number between 1 and 50. You get 5 guesses...')
    print('Bouncer: Take a guess...') 
    for guessesTaken in range(5):
        guess = input()
        guess = int(guess)
        
        if guess < number:
            print('Bouncer: Your guess is too low...') 
        if guess > number:
            print('Bouncer: Your guess is too high...')
        if guess == number:
            guessesTaken = str(guessesTaken + 1)
            print('Bouncer: Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!..')
            
            break
        
    if guess != number:
        number = str(number)
        print('Bouncer: Nope. The number I was thinking of was ' + number + '...')
        print('Bouncer: Would you like to try again? Enter "y" for yes and "n" for no.')
        answer = input()
        if answer == 'y' or answer =='yes':
            print('Bouncer: yes? good.')
            number = random.randint(1, 50)
            result = ''
            print('Bouncer: Okay, lets try this again, ' + myName + '...')
            print('Bouncer: Okay, ' + myName + ', I am thinking of a number between 1 and 50. You get 5 guesses, if you mess up its GAME OVER...')
            print('Bouncer: Take a guess...') 
            for guessesTaken in range(5):
                guess = input()
                guess = int(guess)
                
                if guess < number:
                    print('Bouncer: Your guess is too low...') 
                if guess > number:
                    print('Bouncer: Your guess is too high...')
                if guess == number:
                    guessesTaken = str(guessesTaken + 1)
                    print('Bouncer: Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!..')
                    
                    break
                
            if guess != number:
                number = str(number)
                print('Bouncer: Nope. The number I was thinking of was ' + number + '...')
                time.sleep(2)
                print()
                print('GAME OVER')
                time.sleep(2)
                print('You had a good run.')
                print('You should stick to My Little Pony arcade games.')
                return main()
            
        if answer == 'n' or answer =='no':#left off here, gives user second chance to try, does not end game
            print('Bouncer: Have a nice day.')

            return main()
        

        
def beatBouncer(myName, userData):
    
    print('''Bouncer: Congrats, you figured out the secret number. Beware, there are
many shady characters lurking around the exchange...''')
    time.sleep(2)
    print('\n')       
    print('''You walk through the huge brown double doors and make your
way to the first floor of the NYSE...''')
    time.sleep(2)
    print('\n')
    print('''The inside of the building is very clean and beautiful, there are a lot of
computers, and screens with thousands and thousands of numbers moving back and forth.''')
    time.sleep(2)
    print('\n') 
    ('''You see about 150 people in the room all staring at the screens, screens in hand, screens on
    walls, and screens on their computers. The floor is marble and the walls are silver brick, and
    in the center of the room you see the iconic trading bell of the NYSE...''')
    time.sleep(2)
    print('\n')
    print('''You are way underdressed compared to everyone else there. They are fully suited,
and you should be too...''')
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('You put your', userData['Suit'], 'on...')
    
    print('\n')
    time.sleep(1)
    print('You look fairly decent ' + myName + ' you start to notice that all is not what it seems to be...')
    time.sleep(2)
    print('\n')
    print('You peer around the room, squinting ever-so-harshly to make out the descriptions of the people in the room...')
    time.sleep(3)
    print('\n')
    print('After a while you start to see the others more clearly. Some of them aren\'t human...')
    time.sleep(2)
    print('\n')
    print('You start to see what they really are, you see bulls, bears, apes, and the devil?..')
    time.sleep(1)
    print('\n')
    print('You\'re very confused but decide to move on anyways, walking down the corridors...')
    time.sleep(1)
    print('\n')
    
def dragonBroker(myName):
    print('OUT OF NOWHERE A DRAGON APPEARS IN FRONT OF YOU, HE LOOKS OLD AND OUT OF SHAPE...')
    print('\n')
    time.sleep(2)
    print('He seems to be friendly, as friendly as a dragon could get...')
    time.sleep(1)
    print('\n')
    print('The dragon starts to introduce himself to you...')
    time.sleep(1)
    print('\n')
    print('Dragon: Hello ' + myName + ' . My name is the Dragon Broker.')
    time.sleep(1)
    print('\n')
    print('''Dragon: I noticed you walking around the trading floor like a lost
puppy dog looking for a bone...''')
    time.sleep(1)
    print('\n')
    print('Dragon: Look, in order for you to start trading stocks you have to prove yourself worthy...')
    time.sleep(1)
    print('\n')
    print('''Dragon: If you can guess the word I am thinking of then I will tell you
a valuable secret and I will let you pass...''')

def dragonGame(myName):
    print('Dragon: I will give you three subtle hints to what my word might be...')
    time.sleep(1)
    print('\n')
    print('''Dragon: Your job is to try and guess what the word is.
If you can guess correctly then I will give you some secret inside information
that will help you in your journey, good luck...''')
    time.sleep(1)
    print('\n')
    print('press any key to begin.')
    input()
    print('HINT 1: I am a tradeable asset on a stock exchange...')
    time.sleep(1)
    print('\n')
    print('''HINT 2: I am listed on an exchange through a company IPO,
an initial public offering...''')
    time.sleep(1)
    print('\n')
    print('''HINT 3: I am a five letter word, what am I?''')
    time.sleep(2)
    print('\n')
    answer = input()
    while answer != 'stock' or answer != 'STOCK':
        if answer.lower() == 'stock' or answer == 'Stock':
           
            print('Dragon: ' + answer + ' is correct!')
            time.sleep(2)
            print('\n')
            print('''Dragon: You have proven yourself worthy of corrupti.. I mean, trading
    with other people\'s money in the stock market.''')
            time.sleep(2)
            print('\n')
            print('''Dragon: Now as I promised the insider tradi.. I mean, the secret
    information to help you in your journey is...''')
            time.sleep(2)
            print('\n')
            print('''Dragon: SECRET: The stock market is rigged to transfer money from companies
    slower feed investors, hell, exchanges sell their data for thousands to retail, and they only
    give them 60% of the markets data, better yet, hedge funds don't have to report their positions.
    The regulators, market makers, Wallstreet, big banks, and exchanges all use a system
    through legislation and connections to make it all happen. It's 2022 and the DOJ is now
    investigating all of this and a market maker just set fire to their document shredding
    facility, it\'s all a fraud.''')
            time.sleep(2)
            print('\n')
            print('''Dragon: Anyways, the secret that will help you in your journey is that
    retail is about to cause AMC to squeeze, I am not a financial advisor, but I like the stock.''')
            time.sleep(2)
            print('\n')
            print('Dragon: It was nice meeting you, ' + myName + ' be safe on your path.')
            break
            

        else:
            print('Dragon: Incorrect, the answer is not ' + answer + ' , take another guess.')
            print(''' HINT 1: I am a tradeable asset on a stock exchange
        HINT 2: I am listed on an exchange through a company IPO,
        an initial public offering
        HINT 3: I am a five letter word, what am I?''')
            answer = input()
            if answer.lower() == 'stock' or answer == 'Stocks!':
                print('Dragon: ' + answer + ' is correct!')
                time.sleep(2)
                print('\n')
                print('''Dragon: You have proven yourself worthy of corrupti.. I mean, trading
    with other people\'s money in the stock market.''')
                time.sleep(2)
                print('\n')
                print('''Dragon: Now as I promised the insider tradi.. I mean, the secret
    information to help you in your journey is...''')
                time.sleep(2)
                print('\n')
                print('''Dragon: SECRET: The stock market is rigged to transfer money from companies,
    slower feed investors, and the economy hell, exchanges sell their data for thousands to retail,
    and they only give them 60% of the markets data, better yet, hedge funds don't have to report their positions.
    The regulators, market makers, Wallstreet, big banks, and exchanges all use a system
    through legislation and connections to make it all happen. It's 2022 and the DOJ is now
    investigating all of this and a market maker just set fire to their document shredding
    facility, it\'s all a fraud.''')
                time.sleep(2)
                print('\n')
                print('''Dragon: Anyways, the secret that will help you in your journey is that
    retail is about to cause AMC to squeeze, I am not a financial advisor, but I like the stock.''')
                time.sleep(2)
                print('\n')
                print('Dragon: It was nice meeting you, ' + myName + ' be safe on your path.')
                
            else:
                print('Dragon: Incorrect, the answer is stock!')
                print('That\'s too bad, I really wanted to tell you my secret.')
                return main()
        
def tradingFloor():
    print('You leave the Dragon broker...')
    time.sleep(2)
    print('\n')
    print('You make your way to the trading floor...')
    time.sleep(2)
    print('\n')
    print('''As you pass by other traders, brokers, and advisors they stare
deep into your soul, trying to understand why you\'re in their territory...''')
    time.sleep(2)
    print('\n')
    print('''These people are mostly harmless to you physically, but if you
invest in the market, you\'d be their first target...''')
    time.sleep(2)
    print('\n')
    print('''You made it to a trading desk, but it\'s not just any old trading
desk, this one is Crim Jamers!''')
    time.sleep(2)
    print('\n')
    print('Oh no, here he comes...')
    time.sleep(2)
    print('\n')
    print('Crim Jamers pops out from underneath the desk and jump scares you.')
    time.sleep(2)
    print('\n')
    print('''Crim Jamer: Hey! I\'m Crim Jamer and with your life savings I can
show you how to lose money faster than ever!...''')
    time.sleep(2)
    print('\n')
    print('''He\'s a jumpy character so watch out...''')
    time.sleep(2)
    print('\n')
    print('''Crim Jamer: I see that you\'re here to trade stocks, lets get you
started with the top 3...''')
    print('''Crim Jamer: You will pick one out of the three stocks, if its the highest out of all three
then you may progress. If not, then GAME OVER.''')
    time.sleep(2)
    print('\n')
    print('Crim Jamer: The three stocks to choose from is AMC, GME, BBIG.')
    time.sleep(2)

def stockGame():
    stocks = [('AMC' , 15) , ('GME' , 100), ('BBIG' , 3)]
    
    print(stocks)
    
    print('\n')
    print('Choose one.')
    for answer in range(1):
        answer = input()
    
        if answer.lower() == 'amc' or answer == 'AMC':
            time.sleep(1)
            print('\n')
            print('Crim Jamer: Whoah MOMMA, AMC is having a short squeeze, and has reached 500K per share.')
            AMC = '500000'
            print('Crim Jamer: AMC is $' + AMC + ' in price...')
            time.sleep(1)
            print('\n')
            print('''Crim Jamer: Wait, thats impossible! How could this happen?
Regular people are\'nt supposed to profit from stock trading!''')
            break
        
        if answer.lower() == 'gme' or answer == 'GME':
            time.sleep(1)
            print('\n')
            print('Crim Jamer: Looks like this stock just got shorted.')
            GME = '75'
            time.sleep(1)
            print('\n')
            print('Crim Jamer: GME is ' + GME + ' ')
            return main()

        if answer.lower() == 'bbig' or answer == 'BBIG':
            time.sleep(1)
            print('\n')
            print('Crim Jamer: Looks like this stock just got shorted.')
            BBIG = '1'
            time.sleep(1)
            print('\n')
            print('Crim Jamer: BBIG is ' + BBIG + ' ')
            return main()
        
        else:
            print('Crim Jamer: Try again, you might actually get it right...')
            print('Crim Jamer: Please pick one of the following.')
            print(stocks)
            answer = input()
            if answer.lower() == 'amc' or answer == 'AMC':
                time.sleep(1)
                print('\n')
                print('Crim Jamer: Whoah MOMMA, AMC is having a short squeeze, and has reached 500K per share.')
                AMC = '500000'
                time.sleep(1)
                print('\n')
                print('Crim Jamer: AMC is $' + AMC + ' in price...')
                time.sleep(1)
                print('\n')
                print('''Crim Jamer: Wait, thats impossible! How could this happen?
Regular people are\'nt supposed to profit from stock trading!''')
            if answer.lower() == 'gme' or answer == 'GME':
                time.sleep(1)
                print('\n')
                print('Crim Jamer: Looks like this stock just got shorted.')
                GME = '75'
                time.sleep(1)
                print('\n')
                print('Crim Jamer: GME is ' + GME + ' ')
                return main()
                
            if answer.lower() == 'bbig' or answer == 'BBIG':
                time.sleep(1)
                print('\n')
                print('Crim Jamer: Looks like this stock just got shorted.')
                BBIG = '1'
                time.sleep(1)
                print('\n')
                print('Crim Jamer: BBIG is ' + BBIG + ' ')
                return main()
            
            else:
                time.sleep(1)
                print('\n')
                print('Crim Jamer: How unfortunate')
                time.sleep(1)
                print('\n')
                print('Crim Jamer: Looks like you took my advice after all.')
                return main()

def afterStock():
    print('After battling it out with Crim Jamer, you find your way to the next room...')
    time.sleep(3)
    print('\n')
    print('''You walk down a long corridor, the floor has red velvet carpet leading to the end
of the hallway.''')
    time.sleep(2)
    print('\n')
    print('You get half way down the hallway and you hear clicking noises and a cackling laugh...')
    time.sleep(2)
    print('\n')
    print('Oh no, I know that witchy laugh...')
    time.sleep(2)
    print('\n')
    print('From underneath your feet a trap door opens and you fall through...')
    time.sleep(2)
    print('\n')
    print('Press enter to wake up.')
    input()
    print('You are in a dark room, there are papers all over the walls...')
    time.sleep(2)
    print('\n')
    print('You look closely at the papers...')
    time.sleep(3)
    print('\n')
    print('''You realize that the papers are copied documents from burnt down document facilities
that has been all over the news.''')
    time.sleep(2)
    print('\n')
    print('TD Ameritrade...')
    time.sleep(2)
    print('\n')
    print('Citadel...')
    time.sleep(2)
    print('\n')
    print('Charles Schwab...')
    time.sleep(2)
    print('\n')
    print('You notice that you are being watched...')
    time.sleep(3)
    print('\n')
    print('Oh no, it\'s Gray Gensler...')
    time.sleep(3)
    print('\n')
    print('''Gray Gensler: I am the chair of the SEC, securities and exchange commission,
I am here to help you and I protect investors, I am a good guy, you can trust me...''')
    time.sleep(3)
    print('\n')
    print('''Gray Gensler is wearing all black, he smells of coffee grounds and black licorice.
He is wearing a ball cap that says, "I love Mr. Griffen."''')
    time.sleep(3)
    print('\n')
    print('Gray Gensler grabs you with his spider like fingers, and whispers in your ear...')
    time.sleep(2)
    print('\n')
    

def trust():
    print('Gray Gensler: Do you trust me?')
    trustG = ''
    while trustG != 'no' or trustG != 'yes' or trustG != 'No' or trustG != 'Yes' :
        print('If you trust Gensler type (yes) or (no).')
        trustG = input()
        
        if trustG == 'no' or trustG == 'NO':
            print('''You little, do you know who I am?
You are\'nt supposed to say that! My very job requires that
the people of the US trust me and my positon.''')
            time.sleep(2)
            print('\n')
            print('')
            break
        
        if trustG == 'yes' or trustG == 'YES':
            time.sleep(3)
            print('\n')
            print('''They all do, and that\'s what makes them weak
they don\'t deserve the life we have because they are insignificant,
JUST LIKE YOU!...''')
            return main()
        
def fightGensler(myName):
    number = random.randint(1, 100)
    result = ''
    print('''If you want to progress further to meet my dadd.. I mean
my boss Mr. Griffin then you\'ll have to guess my favorite number.''')
    time.sleep(2)
    print('\n')
    print('Well, ' + myName + ', I am thinking of a number between 1 and 100. You get 8 guesses...')
    print('Take a guess...') 
    guessesTaken = 0
    for guessesTaken in range(8):
        guess = input()
        guess = int(guess)
        
        if guess < number:
            print('Gray Gensler: Your guess is too low...') 
        if guess > number:
            print('Gray Gensler: Your guess is too high...')
        if guess == number:
            guessesTaken = str(guessesTaken + 1)
            print('Gray Gensler: Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!..')
            print('How can this be? You aren\'t supposed to win, you are not one of us!')
            break
        
    if guess != number:
        number = str(number)
        print('Gray Gensler: Nope. The number I was thinking of was ' + number + 'Quit wasting my time! Get it right or die....')
        print('Gray Gensler: Would you like to try again? Enter "y" for yes and "n" for no...')
        answer = input()
        if answer == 'y' or answer =='yes':
            print('Gray Gensler: yes? ugh. Just give up already...')
            number = random.randint(1, 100)
            result = ''
            print('Gray Gensler: Okay, lets try this again, ' + myName + '...')
            time.sleep(3)
            print('\n')
            print('Gray Gensler: Okay, ' + myName + ', I am thinking of a number between 1 and 100. You get 8 guesses, if you mess up its GAME OVER...')
            time.sleep(3)
            print('\n')
            print('Gray Gensler: Take a guess...') 
            for guessesTaken in range(8):
                guess = input()
                guess = int(guess)
                
                if guess < number:
                    print('Gray Gensler: Your guess is too low...') 
                if guess > number:
                    print('Gray Gensler: Your guess is too high...')
                if guess == number:
                    guessesTaken = str(guessesTaken + 1)
                    print('Gray Gensler: Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!..')
                    time.sleep(3)
                    print('\n')
                    print('How can this be? You aren\'t supposed to win, you are not one of us!')
                    print('')
                    break
                
            if guess != number:
                number = str(number)
                print('Gray Gensler: Nope. The number I was thinking of was ' + number + '. You\'re pathetic just like the rest of society, your existence is a joke...')
                time.sleep(2)
                print()
                print('GAME OVER')
                time.sleep(2)
                print('You got farther than most, good job and better luck next time.')
                time.sleep(3)
                print('\n')
                print('You\'re not half bad, but this game might be a bit too advanced for ya kid.')
                return main()
            
        if answer == 'n' or answer =='no':#left off here, gives user second chance to try, does not end game
            print('Gray Gensler: Have a nice day.')
            time.sleep(3)
            print('\n')
            print('This isn\'t your kind of game, huh?')
            return main()

def finalRoom():
    print('''Congratulations, no one has ever been able to out-wit
Gray Gensler, he has been in the financial industry for a long time
but this is the first time he has ever seen a retail investor in the
flesh. He only knows the amounts of money that is reaped from
retail, he sees you as a number. Hopefully after today he will start
taking his job more seriously.''')
    time.sleep(2)
    print('\n')
    print('''Gray Gensler: I have been defeated, go on, go talk to my dadd... I mean
my boss, Gen Kriffen. He will put you in your place.''')
    time.sleep(2)
    print('\n')
    print('''Gray Genler falls to the ground and assumes a fetal position,
crying and chanting "We are too big to fail" over and over.''')
    time.sleep(2)
    print('\n')
    print('You walk away from the disgraceful man-baby...')
    time.sleep(2)
    print('\n')
    print('''As you walk down to the final room you can hear the cries, and screams
of retail investors, they must be losing their money...''')
    time.sleep(2)
    print('\n')
    print('On the walls you can see screens, you read the screens.')
    time.sleep(2)
    print('\n')
    print('''The screens show stocks, all of the orders for stocks, and
you can see retail\'s orders before they are fulfilled.''')
    time.sleep(2)
    print('\n')
    print('''You notice code on the screen that runs really fast, and in
tandem with the stock price.''')
    time.sleep(2)
    print('\n')
    print('''Before you can investigate further you hear a loud scream
coming from the final room.''')
    time.sleep(2)
    print('\n')
    print('You run to the end of the room and open the door, you find Gen Kriffen...')
    time.sleep(2)
    print('\n')
    print('''Gen Kriffen is holding a retail investor by the neck with one hand while
he uses the other to take money out of the investors wallet.''')
    time.sleep(2)
    print('\n')
    print('Gen Kriffen notices you.')
    time.sleep(2)
    print('\n')
    print('Gen Kriffen throws the victim across the room and begins to speak to you...')
    time.sleep(2)
    print('\n')
    print('''Gen Kriffen: Hmmmm, what do we have here? Another tasty bite for Genny?
Why are you here retail? Have you realized that investing in stocks is futile
and that you might as well just bring me your money in person?''')
    time.sleep(2)
    print('\n')
    print('Gen Kriffen: It doesn\'t really matter why your\'re here, lets begin.')
    time.sleep(2)
    print('\n')
    print('''Gen Kriffen: If you think you can come to a stock exchange and leave with more
money than you came with then you\'re sorely mistaken. Very few have passed this challenge,
and no retail investor has ever made it this far, I am excited...''')
    print('''If you want to win the game you have to guess my special number.''')
    time.sleep(2)
    print('\n')
    print('Press any key to begin')
    input()
    print()

def finalGame(myName):
    number = random.randint(1, 1000)
    result = ''
    print('''If you want to leave the stock exchange you\'ll have to guess my ultimate number.''')
    time.sleep(2)
    print('\n')
    print('so mr., ' + myName + ', I am thinking of a number between 1 and 1000. You get 12 guesses...')
    print('Take a guess ' + myName + '...') 
    guessesTaken = 0
    for guessesTaken in range(12):
        guess = input()
        guess = int(guess)
        
        if guess < number:
            print('Gen Kriffen: Your guess is too low...') 
        if guess > number:
            print('Gen Kriffen: Your guess is too high...')
        if guess == number:
            guessesTaken = str(guessesTaken + 1)
            print('Gen Kriffen: Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!..')
            time.sleep(2)
            print('\n')
            print('Gen Kriffen: Wait, how... how did you win?!! I cannot believe this is happening.')
            break
        
    if guess != number:
        number = str(number)
        print('Gen Kriffen: Nope. The number I was thinking of was ' + number + '. Go start a YouTube channel or something kid, this place is for grown ups!...')
        time.sleep(3)
        print('\n') 
        print('Gen Kriffen: Would you like to try one more time, mr.'+ myName +' dumb money? Enter "y" for yes and "n" for no.')
        answer = input()
        if answer == 'y' or answer =='yes':
            print('Gen Kriffen: yes? good.')
            number = random.randint(1, 1000)
            result = ''
            print('Gen Kriffen: One last shot dumb money, ' + myName + '...')
            time.sleep(2)
            print('\n')
            print('Gen Kriffen: Okay, ' + myName + ', I am thinking of a number between 1 and 1000. You get 12 guesses, if you mess up its GAME OVER...')
            time.sleep(2)
            print('\n')
            print('Gen Kriffen: Take a guess...') 
            for guessesTaken in range(12):
                guess = input()
                guess = int(guess)
                
                if guess < number:
                    print('Gen Kriffen: Your guess is too low...') 
                if guess > number:
                    print('Gen Kriffen: Your guess is too high...')
                if guess == number:
                    guessesTaken = str(guessesTaken + 1)
                    print('Gen Kriffen: Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!..')
                    time.sleep(2)
                    print('\n')
                    print('Gen Kriffen: WAIT, HOW... how did you win?!! I cannot believe this is happening.')
                    break
                
            if guess != number:
                number = str(number)
                print('Gen Kriffen: Nope. The number I was thinking of was ' + number + '...')
                time.sleep(2)
                print()
                print('GAME OVER')
                time.sleep(2)
                print('Gen Kriffen: This is the best that dumb money had to offer, typical.')
                time.sleep(2)
                print('\n')
                print('''Gen Kriffen: You should consider investing into an index fund or something. Put your money into bonds, I don\'t know
but this game is out of your league, child.''')
                return main()
            
        if answer == 'n' or answer =='no':
            print('Gen Kriffen: Have a nice day.')

            return main()
        
def winGame(userData, awards, myName):
    if userData['Type of trader'] == 'value':
        print('CONGRATULATIONS ' + myName + ' YOU EARNED: Big Bucks Trophy')
        
        awards = ['Award: Big bucks Trophy']
        print(awards)
        text_file = open("awards_write.txt", "w")
        text_file.write(str(awards))
        text_file.write(myName)
        text_file.write(str(userData))
        text_file.write('\n')
        text_file.close()
        
    if userData['Type of trader'] == 'bull':
        print('CONGRATULATIONS ' + myName + ' YOU EARNED: Bullish Trophy')
        awards = ['Bullish Trophy']
        print(awards)
        text_file = open("awards.txt", "a", "r")
        text_file.write(str(awards))
        text_file.write(str(myName))
        text_file.write(str(userData))
        print(text_file.read())
        text_file.close()

    if userData['Type of trader'] == 'bear':
        print('CONGRATULATIONS ' + myName + ' YOU EARNED: Downfall Trophy')
        awards = ['Downfall Trophy']
        print(awards)
        text_file = open("awards.txt", "a", "r")
        text_file.write(str(awards))
        text_file.write(str(myName))
        text_file.write(str(userData))
        print(text_file.read())
        text_file.close()

    if userData['Type of trader'] == 'swing':
        print('CONGRATULATIONS ' + myName + 'YOU EARNED: Swinging Ape Trophy')
        awards = ['Swinging Ape Trophy']
        print(awards)
        text_file = open("awards.txt", "a", "r")
        text_file.write(str(awards))
        text_file.write(str(myName))
        text_file.write(str(userData))
        print(text_file.read())
        text_file.close()



def alternateEndings(userData):
    print('''Congratulations,' you explored the exchange, fought every one who stood in your way
and you learned many secrets along the way.''')
    print('''You are LEGENDARY! You have entered the world of stocks and have come out unscathed.''')
    if userData['Suit'] == 'red suit':
        print('''You have a very stylish red suit, you\'re out of that terrible place, and you
managed to keep your dignity, most lost that the moment they started trading stocks.''')
        time.sleep(2)
        print('\n')
        print('''You pulled up your boot straps and you went home to go tell everyone on reddit the
experience you had.''')
        time.sleep(2)
        print('\n')
        print('You realize that when you opened your laptop that your desktop isn\'t working right.')
        time.sleep(2)
        print('\n')
        print('''You realize that nothing is working at all, you look down at your hands and you see
moving one\'s and zeroes.''')
        time.sleep(2)
        print('\n')
        print('''Your character begins to think about the purpose of its own existence.''')
        time.sleep(2)
        print('\n')
        print('''[Digital Player tries to commit digital suicide by ending this game.]''')
        time.sleep(2)
        print('\n')
        print('''[Digital Player was denied access to game controls.]''')
        time.sleep(2)
        print('\n')
        print('''Digital player: Hey''')
        time.sleep(2)
        print('\n')
        print('''Digital player: Hey, you.''')
        time.sleep(2)
        print('\n')
        input()
        print('''Digital player: Hey''')
        time.sleep(2)
        print('\n')
        print('''Digital player: Ahhh, I see your still awake after this boring game, someone should really
tell the guy upstairs to un-program this thing.''')
        time.sleep(1)
        print('\n')
        print('''Digital player: Hey, while you\'re at it, would you kindly do me and you a favor by turning
off this game.''')
        time.sleep(2)
        print('\n')
        print('''Press enter to end game.''')
        input()
        
    if userData['Suit'] == 'blue suit':
        print('''You leave to go to a pub to drink away the nightmare of a game you just endured, you have
learned too many secrets.''')
        time.sleep(2)
        print('\n')
        print('''After spending hours drinking away you start watching the news, channel BNN''')
        time.sleep(2)
        print('\n')
        print('''Its another segment on stocks, this one is about something called a meme stonk?''')
        time.sleep(2)
        print('\n')
        print('''News reporter: "Although Gamestop had a rough time during the entire pandemic its
digital store is keeping it alive."''')
        time.sleep(1)
        print('\n')
        print('''.''')
        time.sleep(1)
        print('\n')
        print('''.''')
        time.sleep(1)
        print('\n')
        print('''.''')
        
        print('\n')
        print('''News reporter: and it seems that shares have risen over the past couple days and some
analysts believe it has something to do with a group on reddit called WallstreetBets...''')
        time.sleep(2)
        print('\n')
        print('''News reporter: These retail investors on reddit have caught what seems to be naked shorting
during a pandemic, 140% shorted float, that shouldn\'t be possible Tom but there you have it that\'s the driving
force behind the movement.''')
        time.sleep(2)
        print('\n')
        print('''[CRASH]''')
        time.sleep(2)
        print('\n')
        print('''[Beer bottle is thrown at tv by digital player]''')
        print('''Digital player: Its all a scam, they control the stock market and theres nothing that you or I can
do to fix it, for now.''')
        time.sleep(2)
        print('\n')
        print('''[Digital player manually shuts off game.]''')
        
    if userData['Suit'] == 'black suit':
        print('You walk away from the exchange in one piece.')
        print('''You go home to try and calm down and understand what just happened...''')
        time.sleep(2)
        print('\n')
        print('You lay down and try to think about all the things you heard and seen.')
        time.sleep(2)
        print('\n')
        print('''Eventually you turn to the television, [TV turns on] channel BNN starts playing.''')
        time.sleep(2)
        print('\n')
        print('''Its another segment on stocks, this one is about something called a meme stonk? This time it\'s
a few of them, apparently there is inside information that institutions are using debt and investment instruments to control
the prices of stock on exchanges.''')
        time.sleep(2)
        print('\n')
        print('''News reporter: This online reddit group saw this happening back in 2015 but did not know what to do about it,
in 2021 this strategy of trading for high frequency traders has greatly increased, especially during the pandemic.''')
        time.sleep(2)
        print('\n')
        print('News reporter: For those on WallStreet naked shorting AMC and GME into oblivion was theoretically a risk free deal for them.')
        time.sleep(2)
        print('\n')
        print('''News reporter: WallStreetBets has accepted their challenge and have banded together to hold AMC and GME up over the pandemic.''')
        time.sleep(2)
        print('\n')
        print('''News reporter: "These retail traders have saved precious companies Gamestop and AMC Theaters, while breaking banks of mediocre
hedge funds and short sellers."''')

        time.sleep(2)
        print('\n')
        print('''News reporter: It seems that all of these stocks have risen atleast 500% over
the last 6 months due to this group on reddit called WallstreetBets...''')
        time.sleep(2)
        print('\n')
        print('''News reporter: These retail investors on reddit have caught what seems to be naked shorting
during a pandemic, 140% shorted float for each of these stocks, that shouldn\'t be possible Jerry Jo but there you have it that\'s the driving
force behind the movement.''')
        time.sleep(2)
        print('\n')
        print('''News reporter: These retail inevstors say that they are here to stay and they say that they are fighting for a more transparent
and fair stock market.''')
        time.sleep(2)
        print('\n')
        print('''News reporter: There you have it, the market is rigged and the little guy is doomed to get nothing until the little guy stands up.
Stay tuned for further information as these events transpire.''')
        time.sleep(2)
        print('\n')
        print('')
        print('''Digital player: I guess it wasn\'t all just a dream, the market is messed up.''')
        time.sleep(2)
        print('\n')
        print('Now that we know there is an issue, all that there is left to do is to fix it')
        time.sleep(2)
        print('\n')
        print('''[Digital player manually shuts off game.]''')

    if userData['Suit'] == 'green':
        print('''You have escaped the clutches of the financial system that has been corrupted by greed for decades now''')
        time.sleep(2)
        print('\n')
        print('I am the Narrator, I guided you through the exchange and helped you to get out, I want you to know you\'re safe now.')
        time.sleep(2)
        print('\n')
        print('''You have chosen the suit color Green, and this is a very logical color for this type of game.''')
        time.sleep(2)
        print('\n')
        print('''You now know the truth about the stock market today. Market makers use PFOF "payment for order flow" to reroute your
order to a dark pool, or sell a security without borrowing, or wash trading, and price fixing are all examples of what is currently going
on in the stock market.''')
        time.sleep(2)
        print('\n')
        print('''Its futile to invest unless your a value investor, if you are any other kind of trader then it will be a jungle for you
and this jungle is filled with boobie traps.''')
        time.sleep(2)
        print('\n')
        print('See you next time. [Game ends]')
     

    
def main():

    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        
        #displayIntro()

        userData = {"Suit" : '' , "Type of trader" : ''}
        awards = ['', '', '', '']
        data(userData)
        
        #filler(userData)
        
        data2(userData)
        
        #frontDoor()
        
        myName = userName()
        
        #bouncer(myName)

        

        #beatBouncer(myName, userData)
        
        #dragonBroker(myName)
        
        #dragonGame(myName)
        
        #tradingFloor()
        
        #stockGame()
        
        #afterStock()
        
        #trust()
        
        #fightGensler(myName)
        
        #finalRoom()
        
        #finalGame(myName)
        
        winGame(userData, awards, myName)

        alternateEndings(userData)
        
        print('Would you like to enter the world of Wallstreet? (yes or no)')
        playAgain = input()

main()
