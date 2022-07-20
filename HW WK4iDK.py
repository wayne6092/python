import time
##inventory = ("hat", "shirt", "pants", "t-shirt", "ball", "knife")
##
##print(inventory)
##
##inventory = []
##
##if not inventory:
##    print("List is empty")
##
##inventory = ["sword", "armor", "shield", "healing potion"]
##
##if "sword" in inventory:
##    print("Got one")
##
##print("\nThe tuple inventory is:\n", inventory)
##
##for item in inventory:
##    print(item)
##
##inventory[0] = "battleaxe"
##
##print(inventory)
##
##print(len(inventory))
##
##print("\nThe tuple inventory is:\n", inventory)
##
##
##print("You have", len(inventory), "items.")
##
##temp1 = inventory[0:2]
##print(inventory)
##print(temp1)
##
##temp1 = inventory[0:4]
##print(inventory)
##print(temp1)
##
##chest = ["gold", "gems"]
##inventory += chest
##print(inventory)
##
##
##inventory.index("healing potion")
##print(inventory)
##
##inventory[4:6] = ["orb of future telling"]
##print(inventory)
##
##inventory.append("frank")
##print(inventory)
##
##inventory.sort()
##print(inventory)
##
##
##inventory.reverse()
##print(inventory)
##
##
##cnt = inventory.count(0)
##print(inventory)
##print("Our gremlins have counted", cnt)
##
##idx = inventory.index("frank")
##print(inventory)
##print(idx)
##
##inventory.insert(4, "frank")
##print(inventory)
##inventory.pop()
##print(inventory)
###Using Keys in dictionaries
##geek = {'404': 'Clueless.', 'Uninstalled': "being fired."}
##print(geek)
##
##print (geek['404'])
##print (geek['Uninstalled'])
##
##if "Dancing Baloney" in geek:
##    print("I know what Dancing Baloney is.")
##else:
##    print("I have no idea what Dancing Baloney is.")
##
##print(geek.get("404"))
##print(geek.get("Dancing Baloney"))
##
##print(geek.get("Dancing Baloney", "I have no idea what dancing Baloney is."))
##
###Adding a key Value pair
##geek["Link Rot"] = "process by which web page links become obsolete."
##print(geek)
###Deleting a key value pair
##del geek['404']
##print(geek)
##
##def list1():
##    item = ''
##    backpack = ["orange", "hammer", "fish", "melting popsicle", "squishy rock"]
##    print("You have awaken")
##    time.sleep(2)
##    print("You look around the all white room, and find a backpack...")
##    time.sleep(1)
##    print('You look through the backpack...')
##    time.sleep(3)
##    print('You find ' + backpack + ' inside the backpack...')
##    print('You are weak and can only choose one, choose carefully guy.')
##    print('Please print item name.')
##    item = input()
##    
##    return item
##
##def list2():
##    item2 = ''
##    suitcase = ["bigger orange", "popsicle stick", "gun", "single toothpick"]
##    print("After you acquired " + item + " You start walking until you find a blue room...")
##    time.sleep(1)
##    print("After walking in circles for hours in the\n blue room you find a suitcase by a door\n at the end of the room, you walk over to it...")
##    time.sleep(2)
##    print("The suitcase opens up, sensing your presence.")
##    print("You found a " + suitcase + " inside the suitcase.")
##    time.sleep(1)
##    print('Unfortunately you are still much too weak, you may only\n pick up one item.')
##    print("Please print item name.")
##    item2 = input()
##    
##    return item2
##
##def chosenItems(item3):
##    item + item2 = item3
##    print("You have chosen " + item3 + " !")
##    print("Now its time to check if these items will get you home.")
##    
##def checkItems(list1, list2):
##    print("I know you are weak and need to go home, but first let me check\n the items you have chosen, and i'll decide whether or not\n you may head home...")
##    time.sleep(3)
##    print("hmmmm...")
##    time.sleep(2)
##    if item3 == suitcase[1:3] or backpack[1:3]
##        print("Great, you're going home.")
##
##    else:
##        print("Game over sonny...")
##    
##playAgain = 'start'
##while playAgain == 'yes' or playAgain == 'y':
##    list1()
##    list2()
##    item3 = 

def list1():
    inventory3 = ''
    inventory = ["sword", "armor", "shield", "healing potion"] 
    inventory2 = ["axe", "knife", "shield", "healing potion"]
    print(inventory)
    print(inventory2)
    inventory3 = inventory + inventory2
    return inventory3
##
##def list2():
##    inventory3 = ''
##    inventory2 = ["axe", "knife", "shield", "healing potion"]
##    print(inventory2 + inventory)
##    inventory3 = inventory + inventory2
##
##    return inventory3
    
def check(checkList):
    if "sword" == inventory3:
        print("Good list")
    else:
        print("Bad list")
    
    
##    if checkList == ('shield'):
##        print("good list.")
##    else:
##        print("bad list.")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    
    list1()
    checkList = inventory3()
    inventory3 = []
    #list2()
    inventory3 = checkList
    check(checkList)

    print('Do you want to play again? (Yes or no?)')
    playAgain = input()














##
##n = ["GME", "AMC", "BBIG"]
##a = [100, 15, 3]
##
##for n, a in zip(n, a):
##    print(n, 'is', a,'Dollars per share currently.')
          

##stocks = ["GME", "AMC", "BBIG"]
##for item in stocks:
##    print(item)
##stocks1 = [("GME", 100),("AMC", 16)("BBIG", 3)]
##stocks1[1] = print(stocks1)
