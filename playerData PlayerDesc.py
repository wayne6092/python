def player(playerData, playerDesc):
    print(playerDesc)
    print('''You can add one skill point to your strength, agility or intelligence
Choose wisely, .''')
    print('press a for strength.')
    print('press b for agility.')
    print('press c for intelligence.')
    Answer = input()
    if Answer == 'a':
        playerDesc['Strength'] = 11
        print(playerDesc)
        #return playerDesc
    if Answer == 'b':
        playerDesc['Agility'] = 5
        print(playerDesc)
        #return playerDesc
    if Answer == 'c':
        playerDesc['Intelligence'] = 2
        print(playerDesc)
        #return playerDesc
    else:
        print('Thats okay, you can add it later.')
    print(playerData)
    print('Player shoots at zombies.')
    playerData[0][1] = 799
    print(playerData)
    playerData[0][1] = 653
    print(playerData)
    playerData[0][1] = 211
    print(playerData)
    playerData[0][1] = 19
    print(playerData)
    playerData[0][1] = 0
    print(playerData)
    if playerData[0][1] == 0:
        print('Go find AMMO soldier, or another weapon!')
    playerData[1][1] = "Laser Beam"
    print('You pick up laser beam.')
    print(playerData)

    return playerData
    

def playerStart(playerData):
   
    playerData[2][1] = "Bad"
    print(playerData)
    print('Oh no, you\'re going to need to grab a health potion.')
    print('''You see a health position on the ground, press 1 to pick
it up, 2 to leave it on the ground''')
    if input() == '1':
        playerData[2][1] = "FULL"
        print(playerData)
    else:
        print('Thats okay, you were\'nt going to beat the high score anyway.')


def next1(playerDesc, playerData):
    print(playerDesc, playerData)


def main():
    playerDesc = {"Strength" : 10, "Agility" : 4, "Intelligence" : 1}
    playerData = [["Ammo", 1000], ["weapon", "Pistol"], ["Health", "Good"]]
    
    playerData = player(playerData, playerDesc)
    
    playerStart(playerData)
   
    next1(playerDesc, playerData)


main()
