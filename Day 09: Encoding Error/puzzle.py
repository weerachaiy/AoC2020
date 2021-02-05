from itertools import combinations
from functools import reduce
import sys

puzzle = [int(line.strip()) for line in open(sys.argv[1], 'r')]
for x in range(25, len(puzzle) + 1, 1):
  if [[2, sorted(ele), sum(ele), reduce(lambda x, y: x * y, ele)] for ele in combinations(puzzle[x-25:x], 2) if sum(ele) == puzzle[x]] == []:
    break
ListB = [puzzle[:x][start:end] for start in range(len(puzzle[:x])) for end in range(start, len(puzzle[:x])) if sum(puzzle[:x][start:end]) == puzzle[x]][0]
print(puzzle[x], max(ListB) + min(ListB))

#testList = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
#Solution2(testList, 5)
