# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  all_levels = _all_tree_paths(root)
  res = []
  for level in all_levels:
    res.append(level[::-1])
  return res


def _all_tree_paths(root):
  if root is None:
    return []

  if root.left is None and root.right is None:
    return [ [root.val] ]

  left_path = _all_tree_paths(root.left) # [['d']]
  right_path = _all_tree_paths(root.right) # [['e']]

  paths = []
  for path in left_path:
    path.append(root.val)
    paths.append(path)
    # paths.append([root.val, *left_path])

  for path in right_path:
    path.append(root.val)
    paths.append(path)

  return paths
