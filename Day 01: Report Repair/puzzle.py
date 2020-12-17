from itertools import combinations
from functools import reduce
import sys

def flatten(li):
  return sum(([x] if not isinstance(x, list) else flatten(x) for x in li), [])

def Solution1(N, Seat):
  S2 = flatten([[N, sorted(ele), sum(ele), reduce(lambda x, y: x * y, ele)] for ele in combinations(puzzle, N) if sum(ele) == Seat])
  print("{}={}".format("+".join([str(x) for x in S2][1:N+1]), S2[N+1]))
  print("{}={}".format("*".join([str(x) for x in S2][1:N+1]), S2[N+2]))

puzzle = [int(line.strip()) for line in open(sys.argv[1], 'r')]
Solution1(2,2020)
Solution1(3,2020)
