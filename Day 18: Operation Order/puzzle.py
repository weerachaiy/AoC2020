import sys

def post_fix(args):
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

operator = set(['+', '-', '*', '/', '(', ')'])
puzzle = [line.strip() for line in open(sys.argv[1], 'r')]
operator_num = {'+':2, '-':2, '*':2, '/':2}
y = 0
for exp in puzzle:
  y += calculator_function(post_fix(exp.strip()))
print("sum: {}".format(y))
operator_num = {'+':2, '-':2, '*':1, '/':1}
y = 0
for exp in puzzle:
  y += calculator_function(post_fix(exp.strip()))
print("sum: {}".format(y))
