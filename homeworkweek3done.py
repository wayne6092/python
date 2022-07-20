def main():
   print('Hello, lets begin.')


    
def compTwolists(list1, list2):
    (list1.sort())
    (list2.sort())
    if(list1==list2):
        return "Equal"
    else:
        return "Not Equal"



main()
list1 = ['apple', 'orange', 'banana']
list2 = ['apple', 'banana', 'orange']
list3 = ['banana', 'orange', 'apple']
list4 = ['orange', 'apple', 'dog']

result = compTwolists(list1, list2)
compTwolists(list1, list2)
print(compTwolists(list1, list2))
print(compTwolists(list2, list3))
print(compTwolists(list3, list4))

##compTwolists(['apple', 'banana', 'orange'])
##compTwolists(['orange', 'grape', 'chips'])
##result = compTwolists(a, b)
##a = ['orange', 'grape', 'chips']
##b = ['apple', 'banana', 'orange']
##compTwolists(result)
##chest = ["gold", "gems"]
##inventory += chest
##print(inventory)
##
##print(len(inventory))
##
##del inventory[1]
##print(inventory)
##
##print("start")
##
##inventory.append("frank")
##print(inventory)
##
##inventory.sort()
##print(inventory)
##
##inventory.reverse()
##print(inventory)
##
##cnt = inventory.count("frank")
##print(cnt)
##
##inventory.index('frank')
##print(inventory)
##
##inventory.insert(1, "bow")
##print(inventory)
