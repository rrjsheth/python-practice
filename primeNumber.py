#prime number code

#ask the user for the nth prime number
#then start with two and keep adding prime numbers to an arr
#then print out the last prime number
from math import sqrt
import sys
HIGHEST_RANGE = 11


#ask the user for input
nthNum = input("enter the nth prime number you want:\n")

primeArr = [2,3,5,7]
primeNum = 4 #how many prime number have been found
num = 11 #start value to check if prime

#start with number 11 and try to find the nth prime number
#for num in range(11,sys.maxint,2):
while True:
#
    #check if the number is divisible by any num in primearr
    for prime in primeArr:
    #
        #if prime arr is greater than square root of that num
        #then it is a prime number
        if prime > sqrt(num):
            break

        remainder = num%prime #if zero then not prime

        #if the number is divisible by a prime num then num is
        #not a prime num
        if remainder == 0:
            break


    #end of inner for loop

    #if we have found the nth prime number
    if primeNum >= nthNum:
        break

    #if number being checked is a prime number then add to arr
    if remainder !=0:
        primeNum+=1
        primeArr.append(num)

    #increment num by two to skip even number
    num+=2
# end of for loop

print str(nthNum) + "th prime number is: " + \
                    str(primeArr[primeNum-1])
