import sys
import time

def flatten(li):
  return sum(([x] if not isinstance(x, list) else flatten(x) for x in li), [])

def bitMask1(n1, n2):
  for x, y in n2:
    if x == 'X':
      continue
    n1 = n1 | 2**y if int(x) else n1 & ~2**y
  return n1

def bitMask2(n1, n2):
  for x, y in n2:
    if x == 'X':
      continue
    n1[0] = n1[0] | 2**y if int(x) else n1[0]
  for x, y in n2:
    if x == 'X':
      n1.append([[n | 2**y, n & ~2**y] for n in n1])
      n1 = list(set(flatten(n1)))
  return n1

def M1(puzzle):
  """
  Machine Type I
  """
  mem1 = {}
  mem2 = {}
  for y in puzzle:
    for x in y.split("="):
      if x.strip() == "mask":
        state = "mask"
        continue
      if x.strip()[:3] == "mem":
        state = "mem"
        idx = int(x.strip()[4:-1])
        continue
      if state == "mask":
        mask = [(y, x) for x, y in enumerate(x.strip()[::-1])]
        continue
      if state == "mem":
        mem1[idx] = bitMask1(int(x.strip()), mask)
        for n in bitMask2([idx], mask):
          mem2[n] = int(x.strip())
  print(sum(mem1.values()), sum(mem2.values()))

def M2(puzzle):
  """
  Machine Type II
  """
  mem1 = {}
  mem2 = {}
  prg = [y.split("=") for y in puzzle]
  for k, v in prg:
    if k.strip() == "mask":
      mask = [(y, x) for x, y in enumerate(v.strip()[::-1])]
      continue
    if k.strip()[:3] == "mem":
      idx = int(k.strip()[4:-1])
      mem1[idx] = bitMask1(int(v.strip()), mask)
      for n in bitMask2([idx], mask):
        mem2[n] = int(v.strip())
  print(sum(mem1.values()), sum(mem2.values()))

puzzle = [line.strip() for line in open(sys.argv[1], 'r')]
starttime = time.time()
M1(puzzle)
print('M1 took {} seconds'.format(time.time() - starttime))
starttime = time.time()
M2(puzzle)
print('M2 took {} seconds'.format(time.time() - starttime))
