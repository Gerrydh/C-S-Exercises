# Gerard Hanlon, 2018-02-08
# Collatz Exercise. If the integer is odd, then multiply by 3 and add 1. If
# the integer is even, then devide by 2. The integer should eventually return 
# the integer 1. 

# n = any integer entered.
n = int(input("Please enter an Integer:"))

# as long as n is a psoitive greater than 1
while n > 1:
  if n % 2 == 0: # if the integer is even
      n = (n // 2) # devide by 2
      print(n) # print if the integer is 1
  elif n % 1 == 0: # or else, if the integer is odd
      n = (n * 3 + 1) # then multiply the integer by 3 and add 1
      print(n) # print if the integer is 1
  else: # or else
     print(n) # print if the integer is 1
