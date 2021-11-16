#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the
# year that they will turn 100 years old.
# Ask the user for another number and printing out that many copies of the previous message.
#Print out that many copies of the previous message on separate lines.

while True:
    name = input("What's ur name: ")
    age = int(input('Age: '))
    current_year = 2019
    birth_year = current_year - age
    birth_year += 100
    output = str(name)+' will be 100 in '+str(birth_year)+'\n'
    number = int(input('Number of copies: '))
    print(number*output)
    print('Do you want exit: ')
    final = input('Y/N ')
    if final == 'y'.lower():
        break



