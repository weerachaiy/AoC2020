puzzle = "193467258"
puzzle = "389125467"
puzzle = [int(x) for x in puzzle]
#s = 0
y = puzzle
for x  in range(len(puzzle)):
  print(y)
  z = y[1:4]
  t = y[4:]
  #print(z)
  #print(t)
  i = y[x]
  f = i-1
  #print("({})".format(i))
  print(f)
  print(t[x:4+x])
  if f in t[x:4+x]:
    print(f)
    t.remove(f)
    puzzle = [i] + [f] + z + t
  else:
    print(max(t))
    puzzle = [i] + t[:4+x]  + z + t[4:-x]
  #print(t)
  print(puzzle)
  #s = 1
