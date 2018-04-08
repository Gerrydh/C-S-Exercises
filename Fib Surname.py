# Gerard Hanlon, 30.01.2018
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci numbers."""
  i = 0 # variable i = the first fibonacci number
  j = 1 # variable j = the second fibonacci number
  n = n - 1 # variable n = n - 1

  while n >= 0: # while n is greater than 0
    i, j = j, i + j # 0, 1 = 1, 0 + 1
    n = n - 1 # we want the script to add the number preceeding it
  
  return i # return the new value of i

name = "Hanlon" # My surname
first = name[0] # The first letter of my Surname- H
last = name [-1] # The last letter of my surname- N
firstno = ord (first) # The fibonacci number for 8- H is the 8th letter in the alphabet
lastno = ord(last) # The fibonacci for number 14- N is the 14th letter in the alphabet
x = firstno + lastno # x = the final fibonacci number we are looking for- The fibonacci numbers of the first and last letters of my surname added together

ans = fib(x) # ans = the fibonacci of x
print("My surname is", name) # prints my surname
print("The first letter", first, "is number", firstno) # returns the fibonacci of the first letter of my surname
print("The last letter", last, "is number", lastno) # returns the fibonacci number of the last letter of my surname
print("Fibonacci number", x, "is", ans) # x = the total fibonacci number
