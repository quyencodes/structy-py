# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

"""

is binary search tree:
in order traversal (left, self, right)
- make a list, add all left children, then self, then right children
- process the list with two pointers, it should be in ascending order

"""

def is_binary_search_tree(root):
  values = []
  inorder_traversal(root, values)

  for i in range(1, len(values) - 1):
    j = i - 1
    prev, curr = values[j], values[i]
    if prev > curr:
      return False

  return True

def inorder_traversal(root, values):
  if root is None:
    return

  inorder_traversal(root.left, values)
  values.append(root.val)
  inorder_traversal(root.right, values)
  return


