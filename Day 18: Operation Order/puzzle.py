import sys

def post_fix(args, operator_num):
  stack = []
  postfix = ''
  for ch in args.replace(" ",""):
    if ch not in operator:
      postfix += ch
    elif ch == '(':
      stack.append('(')
    elif ch == ')':
      while stack and stack[-1] != '(':
        postfix += stack.pop()
      stack.pop()
    else:
      while stack and stack[-1] != '(' and operator_num[ch] <= operator_num[stack[-1]]:
        postfix += stack.pop()
      stack.append(ch)
  while stack:
    postfix += stack.pop()
  return postfix

def calculator_function(args):
  stack = []
  for ch in args:
    if ch not in operator:
      stack.append(int(ch))
    else:
      b = stack.pop()
      a = stack.pop()
      c = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}[ch]
      stack.append(c)
  return stack[-1]

def M1(puzzle, operator_num):
  y = 0
  for exp in puzzle:
    x = post_fix(exp.strip(), operator_num)
    n = calculator_function(x)
    print("{} -> {} = {}".format(exp.strip(), x, n))
    y += n
  print("sum: {}".format(y))

puzzle = [line.strip() for line in open(sys.argv[1], 'r')]
operator = set(['+', '-', '*', '/', '(', ')'])
M1(puzzle, {'+':2, '-':2, '*':2, '/':2})
M1(puzzle, {'+':2, '-':2, '*':1, '/':1})
