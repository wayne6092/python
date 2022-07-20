text_file= open('read_it.txt', 'r')

#String is A1
A1= text_file.readline()
#forces one to be a string (str)
##if str(1) in A1:
##    print('Got one.')
##
##else:
##    print('Nope')
for line in text_file:
    print(line)





#Adding 's' to readline = readlines, this turns text into a list
print(text_file.readlines())

print(text_file.readline())
#line blank, reads all lines one by one
text_file.close()
