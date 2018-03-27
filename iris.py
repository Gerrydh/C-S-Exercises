# Gerard Hanlon. 28.02.2018
# Opening and formatting the Iris Data file

# open the data file and give it the variable name f and then close the file when complete
with open("data/iris.csv") as f:
    for line in f: # read the file line by line
      print(line.split(',') [0:4])
