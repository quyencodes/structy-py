# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
  res = _path_finder(root, target)
  if len(res) == 0:
    return None
  else:
    return res[::-1]


def _path_finder(root, target):
  if root is None:
    return []

  if root.val == target:
    return [root.val]

  left_values = _path_finder(root.left, target)
  if len(left_values) > 0:
    left_values.append(root.val)
    return left_values

  right_values = _path_finder(root.right, target)
  if len(right_values) > 0:
    right_values.append(root.val)
    return right_values

  return []
