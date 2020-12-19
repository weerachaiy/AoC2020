import sys

def operator_num(n):
  if n == "+" or n == "-":
    return 2
  elif n == "(":
    return 3
  elif n == ")":
    return 4
  else:
    return 2

def add(num1,num2):
  return num1 + num2

def minus(num1,num2):
  return num2 - num1

def multi(num1,num2):
  return num1 * num2

def divide(num1,num2):
  return num2 / num1

def post_fix(*args):
  for arg in args:
    if arg not in operator:
      arg = int(arg)
      postfix.append(arg)
    else:
      if len(stack) == 0:
        stack.append(arg)
      else:
        operator_value = operator_num(arg)
        stack_value = operator_num(stack[-1])
        if operator_value > stack_value:
          if operator_value == 4:
            while True:
              postfix.append(stack.pop())
              if stack[-1] == "(":
                stack.pop()
                break
          else:
            stack.append(arg)
        elif operator_value < stack_value:
          if stack[-1] == '(':
            stack.append(arg)
          else:
            while len(stack) > 0:
              if stack[-1] == 3:
                break
              postfix.append(stack.pop())
            stack.append(arg)
        elif operator_value == stack_value:
          if stack_value == 3:
            stack.append(arg)
          else:
            postfix.append((stack.pop()))
            stack.append(arg)
  while len(stack) > 0:
    postfix.append(stack.pop())
  return postfix

def calculator_function(*args):
  while len(postfix) > 1:
    for operate in args:
      if operate in operator:
        arg_index = postfix.index(operate)
        if operate == "+":
          postfix.pop(arg_index)
          result = add(postfix.pop(arg_index - 1), postfix.pop(arg_index - 2))
          postfix.insert(arg_index - 2, result)
        elif operate == "-":
          postfix.pop(arg_index)
          result = minus(postfix.pop(arg_index - 1), postfix.pop(arg_index - 2))
          postfix.insert(arg_index - 2, result)
        elif operate == "*":
          postfix.pop(arg_index)
          result = multi(postfix.pop(arg_index - 1), postfix.pop(arg_index - 2))
          postfix.insert(arg_index - 2, result)
        elif operate == "/":
          postfix.pop(arg_index)
          result = multi(postfix.pop(arg_index - 1), postfix.pop(arg_index - 2))
          postfix.insert(arg_index - 2, result)
      else:
        continue
  return postfix

puzzle = [line.strip() for line in open(sys.argv[1], 'r')]
operator = ["*", "/", "+", "-", "(", ")"]
z = 0
for x in puzzle:
  postfix = []
  stack = []
  y = x.replace("(","( ").replace(")"," )").split()
  post_fix(*y)
  n = int(calculator_function(*postfix)[0])
  z += n
print(z)
