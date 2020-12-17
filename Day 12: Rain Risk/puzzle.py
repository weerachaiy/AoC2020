import sys

def LR(n1, n2, n3):
  idx = n1.index(n2)
  n1 = n1[idx:idx+4]
  idx = n1.index(n1[n3%360//90])
  return n1[idx]

def F(n1, n2, n3, n4):
  if n1 == "E":
    n3 += n2
  if n1 == "W":
    n3 -= n2
  if n1 == "N":
    n4 += n2
  if n1 == "S":
    n4 -= n2
  return n3, n4

def LRW(n, n3, n4):
  if n in ["ES", "NE", "SW", "WN"]:
    n3, n4 = n4, 0-n3
  if n in ["EW", "NS", "SN", "WE"]:
    n3, n4 = 0-n3, 0-n4
  if n in ["EN", "NW", "SE", "WS"]:
    n3, n4 = 0-n4, n3
  return n3, n4

def M3(n = 0):
  NEWS = "NESW"*2
  state = "E"
  x , y = 0, 0
  wpx, wpy = 10, 1
  for a, v in [[s[:1], int(s[1:])] for s in puzzle]:
    if a == "L" or a == "R":
      tmp = state
      state = LR(NEWS[::-1], state, v) if a == "L" else LR(NEWS, state, v)
      wpx, wpy = LRW(tmp + state, wpx, wpy) if(n == 1) else [wpx, wpy]
      continue
    if a == "F":
      x, y = [x + (v * wpx), y + (v * wpy)] if(n == 1) else F(state, v, x, y)
      continue
    if n == 0:
      x, y = F(a, v, x, y)
    if n == 1:
      wpx, wpy = F(a, v, wpx, wpy)
  print(abs(x) + abs(y))

puzzle = [line.strip() for line in open(sys.argv[1], 'r')]
#puzzle = ["F10", "N3", "F7", "R90", "F11"]
M3()
M3(n = 1)
