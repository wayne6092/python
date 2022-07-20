#This is the blackjack module I created myself, Base Classes: HAND



class Hand(object):#base class

    """ A hand of playing cards. """



    def __init__(self):#constructor
        self.cards = []#Attribute, also executes for hand
        
    def __str__(self):#status method
        if self.cards:
           rep = ""
           
           for card in self.cards:
               rep += str(card) + "  "
        else:
            rep = "<empty>\n"
            
        return rep

    def clear(self):
        self.cards = []#member is empty list
        
    def add(self, card):
        self.cards.append(card)
        
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print ("Out of cards!")



class Deck(Hand):#Derived class, gets members and methods for free
    """ A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:#Communicates one suit to each rank one suit at a time.
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards) 

    def deal(self, hands, per_hand = 1):#d1 is self
        for rounds in range(per_hand):#per_hand is a default parameter
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print ("Out of cards!")

class Card(object):#base class
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K"]#List class attributes
    SUITS = ["c", "d", "h", "s"]#populate, these are class attributes
      
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit
        
    def __str__(self):#Status method
        rep = self.rank + self.suit

        return rep


class Player(object):
    """ A player for a game. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep



class Unprintable_Card(Card):

    def __str__(self):
        return "<unprintable>"



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


