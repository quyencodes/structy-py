class Node:
  def __init__(self, val=-1, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def depth_first_values(root):
  res, stack = [], [root]
  if root is None:
    return res

  while stack:
    curr = stack.pop()
    res.append(curr.val)

    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)

  return res


def depth_first_values(root):
  return _depth_first_values(root, [])


def _depth_first_values(root, values):
  if root is None:
    return []

  values.append(root.val)
  _depth_first_values(root.left, values)
  _depth_first_values(root.right, values)

  return values


def depth_first_values(root):
  if root is None:
    return []

  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)

  return [root.val, *left_values, *right_values]
