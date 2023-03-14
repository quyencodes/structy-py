# time - o(n)
# space - o(n)

def depth_first_values(root):
  values, stack = [], [root]
  if root is None: return []
  while stack:
    current = stack.pop()
    values.append(current.val)
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)
  return values

def depth_first_values(root):
  values = []
  _depth_first_values(root, values)
  return values

# time - o(n)
# space - o(n)
def _depth_first_values(root, values):
  if root is None:
    return None

  values.append(root.val)

  _depth_first_values(root.left, values)
  _depth_first_values(root.right, values)

def depth_first_values(root):
  if root is None:
    return []

  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)

  return [root.val, *left_values, *right_values]