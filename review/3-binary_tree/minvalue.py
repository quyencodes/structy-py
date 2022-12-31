# bfs
from math import inf
from collections import deque
def tree_min_value(root):
  if root is None:
    return +inf

  queue = deque([root])
  min_value = +inf

  while queue:
    current = queue.popleft()
    if current.val < min_value:
      min_value = current.val

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return min_value

# dfs
def tree_min_value(root):
  if root is None:
    return +inf

  stack = [root]
  min_value = +inf

  while stack:
    current = stack.pop()
    if current.val < min_value:
      min_value = current.val

    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return min_value

# recursive
def tree_min_value(root):
  if root is None:
    return +inf

  left_values = tree_min_value(root.left)
  right_values = tree_min_value(root.right)

  return min(root.val, left_values, right_values)