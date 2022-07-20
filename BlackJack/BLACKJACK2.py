
from Deck_Sdp import Hand, Deck, Card    #Positionable_Card, Player, Unprintable_Card

#blackjack
##
##
##    
##
class Positionable_Card(Card):#derived class, Card becomes Superclass
    def __init__(self, rank, suit, face_up = True): #modifying the constructor, executing original code and face up(is default parameter, and a member)
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up
        
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep
    
    def flip(self):
        self.is_face_up = not self.is_face_up
##
##
##                    
##class Player(object):
##    """ A player for a game. """
##    def __init__(self, name, score = 0):
##        self.name = name
##        self.score = score
##    def __str__(self):
##        rep = self.name + ":\t" + str(self.score)
##        return rep
##
class Unprintable_Card(Card):

    def __str__(self):
        return "<unprintable>"
    
def main():


#CARDS
    card1 = Card("A", "c")#This is self
    print(card1)
    card2 = Card("A", "d")
    print(card2)
    card3 = Card("A", "h")
    print(card3)
    card4 = Card("A", "s")
    print(card4)
    
    card5 = Card("2", "c")
    print(card5)
    card6 = Card("2", "d")
    print(card6)
    card7 = Card("2", "h")
    print(card7)
    card8 = Card("2", "s")
    print(card8)
    
    card9 = Card("3", "c")
    print(card9)
    card10 = Card("3", "d")
    print(card10)
    card11 = Card("3", "h")
    print(card11)
    card12 = Card("3", "s")
    print(card12)
    
    card13 = Card("4", "c")
    print(card13)
    card14 = Card("4", "d")
    print(card14)
    card15 = Card("4", "h")
    print(card15)
    card16 = Card("4", "s")
    print(card16)

    card17 = Card("5", "c")
    print(card17)
    card18 = Card("5", "d")
    print(card18)
    card19 = Card("5", "h")
    print(card19)
    card20 = Card("5", "s")
    print(card20)
    
    card21 = Card("6", "c")
    print(card21)
    card22 = Card("6", "d")
    print(card22)
    card23 = Card("6", "h")
    print(card23)
    card24 = Card("6", "s")
    print(card24)

    card25 = Card("7", "c")
    print(card25)
    card26 = Card("7", "d")
    print(card26)
    card27 = Card("7", "h")
    print(card27)
    card28 = Card("7", "s")
    print(card28)
    
    card29 = Card("8", "c")
    print(card29)
    card30 = Card("8", "d")
    print(card30)
    card31 = Card("8", "h")
    print(card31)
    card32 = Card("8", "s")
    print(card32)


    card33 = Card("9", "c")
    print(card33)
    card34 = Card("9", "d")
    print(card34)
    card35 = Card("9", "h")
    print(card35)
    card36 = Card("9", "s")
    print(card36)
    
    card37 = Card("10", "c")
    print(card37)
    card38 = Card("10", "d")
    print(card38)
    card39 = Card("10", "h")
    print(card39)
    card40 = Card("10", "s")
    print(card40)

    card41 = Card("J", "c")
    print(card41)
    card42 = Card("J", "d")
    print(card42)
    card43 = Card("J", "h")
    print(card43)
    card44 = Card("J", "s")
    print(card44)
    
    card45 = Card("Q", "c")
    print(card45)
    card46 = Card("Q", "d")
    print(card46)
    card47 = Card("Q", "h")
    print(card47)
    card48 = Card("Q", "s")
    print(card48)

    card49 = Card("K", "c")
    print(card49)
    card50 = Card("K", "d")
    print(card50)
    card51 = Card("K", "h")
    print(card51)
    card52 = Card("K", "s")
    print(card52)


    #HANDS | Cards left: 36-42, 48-52


    deck1 = Deck()


    deck1.populate()
    print('\nOrdered Deck: \n' + str(deck1))

    deck1.shuffle()
    print('\nShuffled Deck: \n' + str(deck1))

  
    

    
    your_hand = print("\nYour Hand.\n")
    your_hand = Hand()
    print(your_hand)

    print(your_hand)
    your_hand.add(card2)
    print(your_hand)
    your_hand.add(card43)
    print(your_hand)

    your_hand.add(card44)
    your_hand.add(card45)
    your_hand.add(card46)
    your_hand.add(card47)
    print(your_hand)
    
    
    George = print("\nGeorge\'s Hand.\n")
    George = Hand()

    print(George)
    George.add(card3)
    print(George)
    George.add(card4)
    print(George)
    George.add(card5)
    print(George)

    Mary = print("\nMary's Hand.\n")
    Mary = Hand()
    print(Mary)
    Mary.add(card6)
    print(Mary)
    Mary.add(card7)
    print(Mary)
    Mary.add(card8)
    print(Mary)

    Johnny = print("\nJohnny's Hand.\n")
    Johnny = Hand()
    print(Johnny)
    Johnny.add(card9)
    print(Johnny)
    Johnny.add(card10)
    print(Johnny)
    Johnny.add(card11)
    print(Johnny)

    Frank = print("\nFrank's Hand.\n")
    Frank = Hand()
    print(Frank)
    Frank.add(card12)
    print(Frank)
    Frank.add(card13)
    print(Frank)
    Frank.add(card14)
    print(Frank)

    Jill = print("\nJill's Hand.\n")
    Jill = Hand()
    print(Jill)
    Jill.add(card15)
    print(Jill)
    Jill.add(card16)
    print(Jill)
    Jill.add(card17)
    print(Jill)
    
    
    George.give(card3, Mary)
    print('\nGeorge gives Mary \n' + str(card3))
    Mary.give(card6, George)
    print('\nMary gives George \n' + str(card6))
    print('\nMary\'s hand: \n' + str(Mary))
    print('\nGeorge\'s hand: \n' + str(George))
    
    Mary.give(card3, Johnny)
    print('\nMary gives Johnny\n' + str(card3))
    Johnny.give(card9, Mary)
    print('\nJohnny give Mary \n' + str(card9))
    print('\nMary\'s hand: \n' + str(Mary))
    print('\nJohnny\'s hand: \n' + str(Johnny))

    Johnny.give(card3, Frank)
    print('\nJohnny gives Frank \n' + str(card3))
    Frank.give(card12, Johnny)
    print('\nFrank gives Johnny \n' + str(card12))
    print('\nJohnny\'s hand: \n' + str(Johnny))
    print('\nFrank\'s hand: \n' + str(Frank))

    Frank.give(card3, Jill)
    print('\nFrank gives Jill \n' + str(card3))
    Jill.give(card15, Frank)
    print('\nJill gives Frank\n' + str(card15))
    print('\nFranks\'s hand: \n' + str(Frank))
    print('\nJill\'s hand: \n' + str(Jill))


    
    your_hand.give(card47, Mary)
    your_hand.give(card46 , George)
    your_hand.give(card45, Frank)
    your_hand.give(card44 , Jill)
    your_hand.give(card43, Johnny)
    print('You give the players one card each.\n')
    print('\nMary\'s Hand: \n' + str(Mary))
    print('\nGeorge\'s Hand: \n' + str(George))
    print('\nFrank\'s Hand: \n' + str(Frank))
    print('\nJill\'s Hand: \n' + str(Jill))
    print('\nJohnny\'s Hand: \n' + str(Johnny))
    print('\nyour_hand: \n' + str(your_hand))
    
    my_hand = print("\nDealers Hand.\n")
    my_hand = Hand()
    print(my_hand)
    my_hand.add(card18)
    print(my_hand)
    my_hand.add(card19)
    print(my_hand)
    my_hand.add(card20)
    print(my_hand)

    
    George = print("\nGeorge\'s Hand.\n")
    George = Hand()
    print(George)
    George.add(card21)
    print(George)
    George.add(card22)
    print(George)
    George.add(card23)
    print(George)

    Mary = print("\nMary's Hand.\n")
    Mary = Hand()
    print(Mary)
    Mary.add(card24)
    print(Mary)
    Mary.add(card25)
    print(Mary)
    Mary.add(card26)
    print(Mary)

    Johnny = print("\nJohnny's Hand.\n")
    Johnny = Hand()
    print(Johnny)
    Johnny.add(card27)
    print(Johnny)
    Johnny.add(card28)
    print(Johnny)
    Johnny.add(card29)
    print(Johnny)

    Frank = print("\nFrank's Hand.\n")
    Frank = Hand()
    print(Frank)
    Frank.add(card30)
    print(Frank)
    Frank.add(card31)
    print(Frank)
    Frank.add(card32)
    print(Frank)

    Jill = print("\nJill's Hand.\n")
    Jill = Hand()
    print(Jill)
    Jill.add(card33)
    print(Jill)
    Jill.add(card34)
    print(Jill)
    Jill.add(card35)
    print(Jill)

    Frank.clear()
    Johnny.clear()
    your_hand.clear()
    my_hand.clear()
    Mary.clear()
    George.clear()
    Jill.clear()

    print(deck1)
    deck1.clear()
    deck1.populate()
    print(deck1)
    print("\n")
    deck1.shuffle()
    print(deck1)

    
    hands = [your_hand, my_hand, George, Mary, Frank, Johnny]
    
    deck1.deal(hands, per_hand = 5)
    print(George)
    print('\n')
    print(Johnny)
    print('\n')
    print(Jill)
    print('\n')
    print(Frank)
    print('\n')
    print(Mary)
    print('\n')
    print(your_hand)
    print('\n')
    print(my_hand)
    print('\n')
    
    deck1.deal(hands, per_hand = 1)
    print(George, "This is George's hand")
    print('\n')
    print(Johnny, "This is Johnny's hand")
    print('\n')
    print(Jill, "This is Jill's hand")
    print('\n')
    print(Frank, "This is Frank's hand")
    print('\n')
    print(Mary, "This is Mary's hand")
    print('\n')
    print(your_hand, "This is Your hand")
    print('\n')
    print(my_hand, "This is my hand hand")
    print('\n')
    
    deck1.deal(hands, per_hand = 1)
    print(George, "This is George's hand")
    print('\n')
    print(Johnny, "This is Johnny's hand")
    print('\n')
    print(Jill, "This is Jill's hand")
    print('\n')
    print(Frank, "This is Frank's hand")
    print('\n')
    print(Mary, "This is Mary's hand")
    print('\n')
    print(your_hand, "This is Your hand")
    print('\n')
    print(my_hand, "This is my hand hand")
    print('\n')
    
    deck1.deal(hands, per_hand = 1)
    print(George, "This is George's hand")
    print('\n')
    print(Johnny, "This is Johnny's hand")
    print('\n')
    print(Jill, "This is Jill's hand")
    print('\n')
    print(Frank, "This is Frank's hand")
    print('\n')
    print(Mary, "This is Mary's hand")
    print('\n')
    print(your_hand, "This is Your hand")
    print('\n')
    print(my_hand, "This is my hand hand")
    print('\n')
    deck1.deal(hands, 2)
    Mary.give(Mary.cards[2], George)
    print("Mary gives George" + str(Mary.cards[2]))


    print(Mary)
    print(George)

    uc1 = Unprintable_Card("ABC", "purple")
    print(uc1)
    pc1 = Positionable_Card("DEF", "Green")
    print(pc1)
    pc2 = Positionable_Card("DEF", "Black", False)
    print(pc2)

    pc2.flip()
    print(pc2)
#DECK

    
main()
