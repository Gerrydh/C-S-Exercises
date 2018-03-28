# Gerard Hanlon, 12.03.2018
# The factorial of a number is the number multiplied by all of the positive numbers less than it
# 3 points to consider, the integer must be positive, and it must be greater than 1
#https://www.w3resource.com/python-exercises/python-functions-exercise-5.php

def factorial(n): # defining the factorial function n(the chosen integer)
    if n == 0: # if the integer is equal to 0
        return 1 # then return 1
    else: # otherwise
        return n * factorial(n-1) # return the integer multiplied by the integer and all of its preceeding numbers
n=int(input("Input a number to calculate the factiorial : ")) # n is the integer that is entered
print(factorial(n)) # display the result
