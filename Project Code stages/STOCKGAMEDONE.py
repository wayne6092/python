import random
class curses.textpad.Textbox(win)
stockPrice = [["AMC", 15], ["GME", 112], ["BBIG", 3]]

GME = stockPrice[1]
BBIG = stockPrice[2]
AMC = stockPrice[0]
AMCP = stockPrice[0][1]
GMEP = stockPrice[1][1]
BBIGP = stockPrice[2][1]
print(stockPrice,' \n')

print('AMC\'s Price is ', stockPrice[0][1] ,' \n')
print('GME\'s Price is ', stockPrice[1][1],' \n')
print('BBIG\'s Price is ', stockPrice[2][1],' \n')

stockPrice[0][1] = random.randint(15, 2000)
stockPrice[1][1] = random.randint(40, 750)
stockPrice[2][1] = random.randint(3, 1100)

print('Please choose one stock.')
##choices = 0
##for choices in range(10):
##    choice = input()

choice = input()
while choice != 'AMC' or choice != 'amc' or choice != 'GME' or choice != 'gme' or choice != 'BBIG' or choice != 'bbig': 
    if choice == 'AMC':
        print(AMC)
        if stockPrice[0][1] <= 100:
            print('All bad')
            print('Try again.')
            choice2 = input()
            print(stockPrice)
            print('Please choose another.')
            if choice2 == 'GME':
                print(GME)
                input()
        if stockPrice[0][1] >= 100:
            print('All good')
            input()
            break
            
    if choice == 'amc':
        print(AMC)
        if stockPrice[0][1] <= 100:
            print('All bad')
            print('Try again.')
            choice2 = input()
            print(stockPrice)
            print('Please choose another.')
            if choice2 == 'GME':
                print(GME)
                input()
                
        if stockPrice[0][1] >= 100:
            print('All good')
            input()
            break
            

