# input - root of binary tree
# output - lists of all the values dfs

def depth_first_values(root):
  if root is None:
    return []

  if root.left is None and root.right is None:
    return [root.val]

  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)

  return [root.val, *left_values, *right_values]

def depth_first_values(root):
  if root is None: return []
  values = []
  stack = [ root ]
  while len(stack) > 0:
    current = stack.pop()
    values.append(current.val)

    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return values