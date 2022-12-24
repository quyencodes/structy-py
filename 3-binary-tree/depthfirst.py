class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# iterative
def depth_first_values(root):
  if root is None:
    return []

  values = []
  stack = [ root ]

  while stack:
    current = stack.pop()
    values.append(current.val)

    if current.right is not None:
      stack.append(current.right)
    if current.left is not None:
      stack.append(current.left)

  return values

def depth_first_values(root):
  if root is None:
    return []

  left_values = depth_first_values(root.left) # [b, d, e]
  right_values = depth_first_values(root.right) # [c, f]
  return [root.val, *left_values, *right_values]
  # return [root.val] + left_values + right_values

#   values = []

#   def depthhelper(current):
#     if current is None:
#       return None

#     if current.left is None:
#       return

#     if current.right is None:
#       return

#     values.append(current.val)
#     if current.left:
#       depthhelper(current.left)
#     else:
#       depthhelper(current.right)

#   depthhelper(root)
#   return values