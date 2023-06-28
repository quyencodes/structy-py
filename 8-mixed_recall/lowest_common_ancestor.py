# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

"""
base cases:

1. get_path(root, val) -> return List
2. return first matching value in both lists

"""

def lowest_common_ancestor(root, val1, val2):
  list1 = get_path(root, val1)
  list2 = get_path(root, val2)
  list2 = set(list2)

  for node in list1:
    if node in list2:
      return node

  return None

def get_path(root, val):
  if root is None:
    return None

  if root.val == val:
    return [val]

  left_path = get_path(root.left, val)
  right_path = get_path(root.right, val)

  if left_path is not None:
    left_path.append(root.val)
    return left_path
  elif right_path is not None:
    right_path.append(root.val)
    return right_path
  else:
    return None