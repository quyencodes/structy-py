# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
  res = _path_finder(root, target)
  if res is None:
    return None
  else:
    return res[::-1]

def _path_finder(root, target):
  if root is None:
    return None

  if root.val == target:
    return [root.val]

  left_path = _path_finder(root.left, target)
  right_path = _path_finder(root.right, target)

  if left_path is not None:
    left_path.append(root.val)
    return left_path

  if right_path is not None:
    right_path.append(root.val)
    return right_path

  return None