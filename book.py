#books if a person will get the same book
from random import shuffle

students = input( "please enter the number of students in a class:\n")

simulations = input( "please enter number of simulations:\n")

classOne = []
classTwo = []
sameTotal = 0 #number of times the class had atleast one student with same book

for index in range(students):
    classOne.append(index)
    classTwo.append(index)

shuffle(classTwo)

for index in range(simulations):
#
    same = False    #if there is a book that is the same
    for i in range(students):
    #
        if classOne[i] == classTwo[i]:
            same = True
    #
    if same:
        sameTotal+=1
        same = False

    shuffle(classTwo)
    shuffle(classOne)
#

print str(float(sameTotal)/simulations) + " is the total number of" + \
                                          " times a student got same book"
