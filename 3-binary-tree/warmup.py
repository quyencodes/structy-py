class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      A
#     / \
#    B   C
#   / \   \
#  D   E   F
#