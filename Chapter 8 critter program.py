#Chapter 8, CRITTERS PROGRAM
class Critter(object):
    """Critter creation"""
    ###LISTS AND TUPLES AND DICTIONARIES CAN BECOME MEMBERS OF THE CLASS###
    #invoking talk method
    #added name attribute(member)-PUBLIC(Directly modifiable)
    total = 0

    def __init__(self, name, mood):
        print('A new critter has been born!')
        self.name = name
        self.__mood = mood 
        Critter.total += 1
    
    def talk(self):
        print("Hi. I'm an instance of class Critter.")


    def __private_method(self):
        print("This is a private method.")
        print("mood: " + self.__mood)

    def public_method(self):
        print("This is a public method.")
        self.__private_method()

        
    def __str__(self):
        rep = "Critter Object\n"
        rep += "name: " + self.name + "\n"
        "Right now I feel", self.__mood, "\n"
        return rep


    def lessThan(self):
        if Critter.total > 1:
            print("Ugh too many")

def main():
    #instantiating object
    crit1 = Critter("Poochie", mood = "happy")
    
    #Creating talk method
    crit1.talk()
    print(crit1)

    print(Critter.total)




    crit2 = Critter("Frank", mood = "crazy")
    crit2.talk()
    print(crit2)

    print(Critter.total) #How many objects
    print(crit1.total) #How many instances
    crit2.lessThan()
    crit1.lessThan()
    crit1.public_method()
    crit2.public_method()

main()
