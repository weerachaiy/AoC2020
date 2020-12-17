import time

def M1(n1, N = 2020):
  count = len(n1)
  while True:
    if count >= N:
      break
    count = count + 1
    if n1[-1] == n1[-2]:
      n1.append(1)
      continue
    if not n1[-1] in n1[:-1]:
      n1.append(0)
      continue
    if n1[-1] in n1[:-1]:
      prev_turn = len(n1)
      recent_spok_bf = prev_turn - n1[:-1][::-1].index(n1[-1]) - 1
      n1.append(prev_turn - recent_spok_bf)
  print(n1[-1])

def M2(n1, N = 2020):
  count = len(n1)
  N1 = [x for x in n1]
  I1 = [y + 1 for y in range(len(n1))]
  while True:
    if count >= N:
      break
    count =  count + 1
    if N1[-1] in N1[:-1]:
      idx = N1.index(N1[-1])
      N1.append(I1[-1]-I1[idx])
      I1.append(count)
      del N1[idx]
      del I1[idx]
    else:
      N1.append(0)
      I1.append(count)
    continue
    if N1[-2] == N1[-1]:
      N1.append(1)
      I1.append(count)
  print(N1[-1])

def M3(n1, N = 2020):
  N1 = [x for x in n1]
  I1 = {}
  for count in range(len(N1) - 1):
    I1[N1[count]] = count
  while True:
    if count >= N - 2:
      break
    count =  count + 1
    if N1[count] in I1:
      N1.append(count-I1[N1[count]])
      I1[N1[count]] = count
    else:
      N1.append(0)
      I1[N1[count]] = count
  print(N1[-1])

#puzzle = [int(x.strip()) for line in open(sys.argv[1], 'r') for x in line.split(",")]
"""
M1([0,3,6])
M1([1,3,2])
M1([2,1,3])
M1([1,2,3])
M1([2,3,1])
M1([3,2,1])
M1([3,1,2])
M2([0,3,6], int(sys.argv[1]))
M2([1,3,2], int(sys.argv[1]))
M2([2,1,3], int(sys.argv[1]))
M2([1,2,3], int(sys.argv[1]))
M2([2,3,1], int(sys.argv[1]))
M2([3,2,1], int(sys.argv[1]))
M2([3,1,2], int(sys.argv[1]))
"""
N = 30000000
starttime = time.time()
M1([2,0,1,7,4,14,18])
print('M1 took {} seconds'.format(time.time() - starttime))
starttime = time.time()
M2([2,0,1,7,4,14,18])
print('M2 took {} seconds'.format(time.time() - starttime))
starttime = time.time()
M3([2,0,1,7,4,14,18])
print('M3 took {} seconds'.format(time.time() - starttime))
starttime = time.time()
M3([2,0,1,7,4,14,18], N)
print('M3 {} took {} seconds'.format(N, time.time() - starttime))
starttime = time.time()
M1([10,16,6,0,1,17])
print('M1 took {} seconds'.format(time.time() - starttime))
starttime = time.time()
M2([10,16,6,0,1,17])
print('M2 took {} seconds'.format(time.time() - starttime))
starttime = time.time()
M3([10,16,6,0,1,17])
print('M3 took {} seconds'.format(time.time() - starttime))
starttime = time.time()
M3([10,16,6,0,1,17], N)
print('M3 {} took {} seconds'.format(N, time.time() - starttime))
starttime = time.time()
M1([14,8,16,0,1,17])
print('M1 took {} seconds'.format(time.time() - starttime))
starttime = time.time()
M2([14,8,16,0,1,17])
print('M2 took {} seconds'.format(time.time() - starttime))
starttime = time.time()
M3([14,8,16,0,1,17])
print('M3 took {} seconds'.format(time.time() - starttime))
starttime = time.time()
M3([14,8,16,0,1,17], N)
print('M3 {} took {} seconds'.format(N, time.time() - starttime))

