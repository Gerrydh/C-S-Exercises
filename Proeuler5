# Gerard Hanlon, 2018-02-22
# Smallest number divisable by number 1-20 (Project Euler Exercise 5)
# https://gist.github.com/PEZ/47534

i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *=j
                break
print (i)
