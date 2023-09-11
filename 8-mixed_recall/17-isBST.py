# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

"""
Create a helper function that adds values of the tree in inorder traversal.

preorder (self, left, right)
inorder (left, self, right)
postorder (left, right, self)
"""


def is_binary_search_tree(root):
  values = []
  traverse_tree(root, values)
  for i in range(1, len(values)):
    j = i - 1
    if values[j] > values[i]:
      return False

  return True


def traverse_tree(root, values):
  if root is None:
    return

  traverse_tree(root.left, values)
  values.append(root.val)
  traverse_tree(root.right, values)
  return
