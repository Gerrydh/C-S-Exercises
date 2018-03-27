# Gerard Hanlon, 23.01.2018 
# A program that displays Fibonacci numbers.
# The fibonacci sequence is a series of numbers where a number is found by adding the sum of the previous 2 numbers

def fib(n):
  #This function returns the nth Fibonacci number.
  i = 0 # variable i = the first fibonacci number
  j = 1 # variable j = the second fibonacci number
  n = n - 1 # variable n = n - 1

  while n >= 0: # while n is greater than 0
    i, j = j, i + j # 0, 1 = 1, 0 + 1
    n = n - 1 # we want the script to add the number preceeding it
  
  return i # return the new value of i

# Test the function with the following value.
x = int(input("Input an integer to calculate the fibonacci number : ")) # Enter any integer to return the fibonacci number
ans = fib(x) # answer = the integer entered from the above instruction
print("Fibonacci number", x, "is", ans) # prints the fibonacci number of the entered integer
