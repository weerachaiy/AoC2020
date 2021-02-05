import sys

maxRC = [127, 7]
FBLR = [64, 32, 16, 8, 4, 2, 1, 4, 2, 1]
seatID = []
puzzle = [line.strip() for line in open(sys.argv[1], 'r')]
for x in puzzle:
  row, column = maxRC
  for y in range(len(x)):
    if x[y] == "F":
      row ^= FBLR[y]
    if x[y] == "B":
      row |= FBLR[y]
    if x[y] == "L":
      column ^= FBLR[y]
    if x[y] == "R":
      column |= FBLR[y]
  seatID.append(row * 8 + column)
row, column = maxRC
for x in range(row + 1):
  for y in range(column + 1):
    if x * 8 + y + 1 in seatID and x * 8 + y - 1 in seatID:
      if not x * 8 + y in seatID:
        print("{} {}".format(max(seatID), x * 8 + y))
