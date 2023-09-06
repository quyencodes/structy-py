# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

"""
DFS helper function. Get path for val1 and val2. Return the earliest intersection between the two lists. Turn one list into a set and do a nested for loop.
"""


def lowest_common_ancestor(root, val1, val2):
  values1 = get_path(root, val1, [])
  values2 = get_path(root, val2, [])

  set2 = set(values2)
  for ele1 in values1:
    if ele1 in set2:
      return ele1


def get_path(root, val, values):
  if root is None:
    return []

  if root.val == val:
    return [root.val]

  left = get_path(root.left, val, values)
  right = get_path(root.right, val, values)

  if left:
    left.append(root.val)
    return left
  if right:
    right.append(root.val)
    return right
