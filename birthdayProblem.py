#birthday problem

#first there is just a mathematical implementation
from random import randint

DAYS_IN_YEAR = 365



classSize = input("the number of students in the class: ")
simulations = input("enter number of simulations: ")
classOne = [] #holds the birthdays of the whole class
sameBirthday = [0] * DAYS_IN_YEAR #checks if any two students has sameBirthday
clrArr = list(sameBirthday) #zero filled arr used to clear sameBirthday arr
sameTotal = 0.0 #how many simulations have atleast 1 pair of ppl w/sameBirthday

#loop the for loop until the whole simulation
for i in range(simulations):
#
    #initialize new list with new birthdays
    for index in range(classSize):
    #
        classOne.append(randint(0,DAYS_IN_YEAR-1))
    #

    #check if any two students have the same birthday
    for index in range(classSize):
    #
        if sameBirthday[ classOne[index] ] == 1:
            sameTotal+=1    #increment if same birthday
            break
        sameBirthday[ classOne[index] ] = 1
    #

    sameBirthday = list(clrArr) #reference a zero filled arr
    classOne = []

#

print str(sameTotal/simulations) +" percentage of time person has same birthday"
