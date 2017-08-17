#Code simulates the probability that if a person retakes a class twice
#then what are the chances that he/she gets the same textbook again


#books if a person will get the same book
from random import shuffle

students = input( "please enter the number of students in a class:\n")

simulations = input( "please enter number of simulations:\n")

#the two arrays that will hold the old and new classes
classOne = []
classTwo = []
sameTotal = 0 #number of times the class had atleast one student with same book

#the for loop will assign the old and shuffle the new class in order
#to simulate a random assignment (same as shuffling textbooks)
for index in range(students):
    classOne.append(index)
    classTwo.append(index)

shuffle(classTwo)

for index in range(simulations):
#
    same = False    
    #if there is a student that got the same textbook
    for i in range(students):
    #
        if classOne[i] == classTwo[i]:
            same = True
            #sameTotal+=1
            #break
    #
    if same:
        sameTotal+=1
        same = False

    shuffle(classTwo)
    shuffle(classOne)
#

print str(float(sameTotal)/simulations) + " is the total number of" + \
                                          " times a student got same book"
