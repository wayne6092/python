##text_file= open('read_it.txt', 'r')
##
###String is A1
##A1= text_file.readline()
###forces one to be a string (str)
####if str(1) in A1:
####    print('Got one.')
####
####else:
####    print('Nope')
##for line in text_file:
##    print(line)
##
##
##
##
##
###Adding 's' to readline = readlines, this turns text into a list
##print(text_file.readlines())
##
##print(text_file.readline())
###line blank, reads all lines one by one
##text_file.close()
text_file = open('write_it.txt', 'a')
text_file.write('Line gS 1\n')
text_file.write('This is line gS 2\n')
text_file.write('That makes this line g 3\n')
#text_file.write(str(1))


lines = ['Line 1\n', 'This is line 2\n', 'That makes this line 3\n']

text_file.writelines(lines)

text_file.close()





text_file= open('write_it.txt', 'r')
for line in text_file:
    print(line)
#String is A1
#A1= text_file.readline()
#forces one to be a string (str)
##if str(1) in A1:
##    print('Got one.')


