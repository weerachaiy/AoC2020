import sys

puzzle = [line for line in open(sys.argv[1]).read().split("\n\n")]
Player = {}
for x in range(len(puzzle)):
  y = puzzle[x].split(":")
  Player[y[0]] = list(y[1].strip().replace("\n", ",").split(","))
print("Player 1: {}".format(Player['Player 1']))
print("Player 2: {}".format(Player['Player 2']))
while len(Player['Player 1']) and len(Player['Player 2']):
  x = int(Player['Player 1'][0])
  del Player['Player 1'][0]
  y = int(Player['Player 2'][0])
  del Player['Player 2'][0]
  if x > y:
    Player['Player 1'].append(str(x))
    Player['Player 1'].append(str(y))
  elif x < y:
    Player['Player 2'].append(str(y))
    Player['Player 2'].append(str(x))
  else:
    Player['Player 1'].append(str(x))
    Player['Player 2'].append(str(y))
print("Fisnish----------")
if Player['Player 2'] ==[]:
  print("Player 1: {}".format(Player['Player 1']))
  print(sum([int(x)*(i+1) for i, x in enumerate(Player['Player 1'][::-1])]))
else:
  print("Player 2: {}".format(Player['Player 2']))
  print(sum([int(x)*(i+1) for i, x in enumerate(Player['Player 2'][::-1])]))
