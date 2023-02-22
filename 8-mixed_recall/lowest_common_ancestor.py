class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def lowest_common_ancestor(root, val1, val2):
  path1 = find_path(root, val1)
  path2 = find_path(root, val2)
  set2 = set(path2)
  for value in path1:
    if value in set2:
      return value


def find_path(root, val):
  if root is None:
    return None

  if root.val == val:
    return [root.val]

  left_path = find_path(root.left, val)
  if left_path is not None:
    left_path.append(root.val)
    return left_path

  right_path = find_path(root.right, val)
  if right_path is not None:
    right_path.append(root.val)
    return right_path

  return None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

lowest_common_ancestor(a, 'd', 'h') # b

