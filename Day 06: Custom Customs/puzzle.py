import sys
from functools import reduce

with open(sys.argv[1]) as file:
  print(sum([len(reduce(lambda x,y: x&y, [set(x) for x in line.split(",")])) for line in file])-1)
