import sys

def nop(state, v, accumulator):
  return state + 1, accumulator

def acc(state, v, accumulator):
  return state + 1, accumulator + v

def jmp(state, v, accumulator):
  return state + v, accumulator

def FixM(n1):
  for x in range(len(n1)):
    fix = ["nop", "jmp"]
    n = [instr for instr in n1]
    k, v = n[x].split()
    if k in fix:
      n[x] = "{} {}".format(fix[not fix.index(k)], v)
    if M(n, 1):
      break

def M(n1, n2 = 0):
  state = 0
  accumulator = 0
  d = {}
  operations = {'nop': nop, 'acc': acc, 'jmp': jmp}
  while state < len(n1) - 1:
    k, v = n1[state].split()
    try:
      if d[str(state)]:
        if n2 == 0:
          print("state: {}, accumulator: {}".format(state, accumulator))
        return False
    except KeyError as e:
      d[str(state)] = n1[state]
    instr = operations[k]
    state, accumulator = instr(state, int(v), accumulator)
  print("state: {}, accumulator: {}".format(state, accumulator))
  return True

List1 = []
for line in open(sys.argv[1]).read().split("\n"):
 List1.append(line)
M(List1)
FixM(List1)
