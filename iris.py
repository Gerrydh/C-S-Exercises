# Gerard Hanlon. 28.02.2018
# Opening and formatting the Iris Data file

# open the data file as f
with open("data/iris.csv") as f:
    for line in f: 
      print(line.split(',') [0:4])
