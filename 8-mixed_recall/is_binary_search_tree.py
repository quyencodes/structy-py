class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def is_binary_search_tree(root):
  values = []
  in_order_traversal(root, values)
  return is_sorted(values)

def in_order_traversal(root, values):
  if root is None:
    return
  in_order_traversal(root.left, values)
  values.append(root.val)
  in_order_traversal(root.right, values)

def is_sorted(numbers):
  for i in range(0, len(numbers) - 1):
    current = numbers[i]
    next = numbers[i + 1]

    if next < current:
      return False

  return True

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def is_binary_search_tree(root):
  res = _is_binary_search_tree(root)
  # print(res)
  return res == sorted(res)


def _is_binary_search_tree(root):
  res = []

  if root is None:
    return None

  # left
  left = _is_binary_search_tree(root.left)
  if left is not None:
    res += left
  # self
  res.append(root.val)
  # right
  right = _is_binary_search_tree(root.right)
  if right is not None:
    res += right

  return res

a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(15)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     18
#  / \     \
# 3   15     19
[3, 5, 15, 12, 18, 19]
values = []
is_binary_search_tree(a) # -> False