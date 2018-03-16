# Gerard Hanlon, 15.03.2018
# A program that displays the Fibonacci numbers

def fibonacci(n): # n returns the nth number
    a,b = 1,1   # define the first two numbers in the sequence
    for i in range(n-1):
        a,b = b, a+b   # move a and b forward 1 unit within each loop. b t will be 1 after that which is a+b
    return a # return the fibonacci number which is the current number
  
x = int(input("Input a number to calculate the Fibonacci :")) # Enter number (x). This will return the given Fibonacci number
ans = fibonacci(x) # The answer is the result of the given integer (x)
print("Fibonacci number", x, "is", ans)
