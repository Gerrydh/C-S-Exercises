# Gerard Hanlon, 2018-02-22
# Smallest number divisable by number 1-20 (Project Euler Exercise 5)
# 3 points to consider. Number must be positive. The number must be evenly divisible. The smallest possible i.
# https://gist.github.com/PEZ/47534

i = 1
for k in (range(1, 21)): # "List" from 1 to 20
    if i / k > 0: # i is +ive
        for j in range(1, 21):
            if (i*j) % k == 0: # i is evenly divisable
                i *=j # return smallest possible i
                break
print (i)
