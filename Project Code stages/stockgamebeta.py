import random
stockPrice = [["AMC", 15], ["GME", 112], ["BBIG", 3]]

print(stockPrice)

print('AMC\'s Price is ', stockPrice[0][1])
print('GME\'s Price is ', stockPrice[1][1])
print('BBIG\'s Price is ', stockPrice[2][1])

stockPrice[0][1] = random.randint(500, 1000)
stockPrice[1][1] = random.randint(10, 750)
stockPrice[2][1] = random.randint(3, 33)
print(stockPrice)

print('AMC\'s Price is ', stockPrice[0][1])
print('GME\'s Price is ', stockPrice[1][1])
print('BBIG\'s Price is ', stockPrice[2][1])

#The first index goes to the first tuple, the second index pulls the value
#print(scores.sort())

name = "location"
score = "Center campus"

#we put name and score in brackets to make "shemp" a list element
stock2 = [["F", 16], ["AMD", 4], ["TSLA", 789]]
#entity = [stock2]
#print(entity)
#adding a tuple
stock2 + stockPrice
stockPrice.append(stock2)
print(stockPrice)

#used two parenthesis because we are removing a single item.
#we changed the parenthesis to brackets
#player.remove(["Location", "Center campus"])
print(stockPrice)

stockPrice.sort[]
print(stockPrice)

for entry in stockPrice:
    stock2 = entry
    print(stockPrice[0][1], "\t", stockPrice[1][1])
    
print(stockPrice)

