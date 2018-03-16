# Gerard Hanlon, 15.03.2018
# A program that displays the Fibonacci numbers

def fibonacci(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
    return a
  
x = int(input("Input a number to calculate the Fibonacci :"))
ans = fibonacci(x)
print("Fibonacci number", x, "is", ans)
