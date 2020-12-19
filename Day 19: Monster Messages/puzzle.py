from anytree import Node, RenderTree
import sys

puzzle = [line for line in open(sys.argv[1]).read().split("\n\n")]
rules = [s.split(":") for s in puzzle[0].split("\n")]
rule = dict(rules)
n = 0
while True:
  x = str(n)
  rootNode = Node(x)
  m1 = rule[x].strip().split()
  print(m1)
  Level11 = Node(m1[0], parent=rootNode)
  Level12 = Node(m1[1], parent=rootNode)
  m21 = rule[m1[0]].strip().split()
  print(m21)
  Level21 = Node(m21[0], parent=Level11)
  m22 = rule[m1[1]].strip().split()
  print(m22)
  Level221 = Node(m22[0], parent=Level12)
  Level222 = Node(m22[1], parent=Level12)
  m32 = rule[m22[1]].strip().split()
  print(m32)
  Level321 = Node(m32[0], parent=Level222)
  Level322 = Node(m32[1], parent=Level222)
  Level323 = Node(m32[3], parent=Level222)
  Level324 = Node(m32[4], parent=Level222)
  m41 = rule[m32[0]].strip().split()
  print(m41)
  m43 = rule[m32[3]].strip().split()
  print(m43)
  Level431 = Node(m41[0], parent=Level321)
  Level433 = Node(m43[0], parent=Level323)
  break  
for pre, fill, node in RenderTree(rootNode):
  print("%s%s" % (pre, node.name))
