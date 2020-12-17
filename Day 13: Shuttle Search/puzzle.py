from itertools import combinations
from functools import reduce
import sys

puzzle = [line.strip() for line in open(sys.argv[1], 'r')]
A = int(puzzle[0])
B = [(int(y), x) for x, y in enumerate(puzzle[1].split(",")) if y != 'x']
D = dict([(x, (A//x+1)*x) for x, y in B])
E = min(D, key = D.get)
F = 1
G = 0
for x, y in B:
  while (G + y) % x:
    G = G + F
  F = F * x
print(A)
print((D[E] - A) * E)
print(G)
