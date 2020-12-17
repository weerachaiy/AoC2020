import sys

def M1(puzzle, N = 2020):
  count = len(puzzle)
  while True:
    if count >= N:
      break
    count = count + 1
    if puzzle[-1] == puzzle[-2]:
      puzzle.append(1)
      continue
    if not puzzle[-1] in puzzle[:-1]:
      puzzle.append(0)
      continue
    if puzzle[-1] in puzzle[:-1]:
      prev_turn = len(puzzle)
      recent_spok_bf = prev_turn - puzzle[:-1][::-1].index(puzzle[-1]) - 1
      puzzle.append(prev_turn - recent_spok_bf)
  print(puzzle[-1])

puzzle = [int(x.strip()) for line in open(sys.argv[1], 'r') for x in line.split(",")]
#M1([0,3,6], N = int(sys.argv[2]))
#M1([1,3,2], N = int(sys.argv[2]))
#M1([2,1,3], N = int(sys.argv[2]))
#M1([1,2,3], N = int(sys.argv[2]))
#M1([2,3,1], N = int(sys.argv[2]))
M1([3,2,1], N = int(sys.argv[2]))
#M1([3,1,2], N = int(sys.argv[2]))
#M1(puzzle, N = int(sys.argv[2]))
