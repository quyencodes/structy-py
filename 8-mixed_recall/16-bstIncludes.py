# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

"""
DFS. Nodes to the left are exclusively less than self. Nodes to the right are exclusively greater than self. Move accordingly and return boolean for the base cases.
"""


def binary_search_tree_includes(root, target):
  return bst(root, target)


def bst(root, target):
  if root is None:
    return False

  if root.val == target:
    return True

  if root.val < target:
    return bst(root.right, target)
  else:
    return bst(root.left, target)
