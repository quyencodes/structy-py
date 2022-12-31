# cant do bfs because we need to find deepest route
def max_path_sum(root):

# dfs
def max_path_sum(root):
  if root is None:
    return None

  max_sum = 0
  stack = [root]
  while stack:
    current = stack.pop()

    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return

from math import inf

# recursive
def max_path_sum(root):
  if root is None:
    return -inf

  if root.left is None and root.right is None:
    return root.val

  left_values = max_path_sum(root.left)
  right_values = max_path_sum(root.right)

  return root.val + max(left_values, right_values)