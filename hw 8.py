class Critter(object):
   """A virtual pet"""
   total = 0
   def __init__(self, name, color, footwear, weapon, shield, helmet, vehicle):
      print ("A new critter has been born!")
      self.name = name
      self.color = color
      self.footwear = footwear
      self.weapon = weapon
      self.shield = shield
      self.helmet = helmet
      self.vehicle = vehicle
      Critter.total = Critter.total + 1
      
   def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        rep += "color: " + self.color + "\n"
        rep += "footwear: " + self.footwear + "\n"
        rep += "weapon: " + self.weapon + "\n"
        rep += "shield: " + self.shield + "\n"
        rep += "helmet: " + self.helmet + "\n"
        rep += "vehicle: " + self.vehicle + "\n"
        return rep
    
   def talk(self):
      print ("Hi. I'm an instance of class Critter.\n")
      print('I love being alive! Hurray!\n')

def main():
    crit1 = Critter("mary", "blue", "sandals", "machete", "garbage can lid", "collander", "skateboard")
    crit1.talk()
    print(crit1)
    crit2 = Critter("frank", "yellow", "slippers", "chainsaw", "paper plate", "bucket", "rollerblades")
    crit2.talk()
    print(crit2)
    crit3 = Critter("lily", "orange", "sneakers", "katana", "umbrella", "baseball helmet", "dirt bike")
    crit3.talk()
    print(crit3)
    crit4 = Critter("jim", "grey", "boots", "gun", "dead critter", "army helmet", "four-wheeler")
    crit4.talk()
    print(crit4)




    print(Critter.total)
    print(crit1.total)
    print(crit2.total)
    print(crit3.total)
    print(crit4.total)
main()

