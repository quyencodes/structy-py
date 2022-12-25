from collections import deque
from math import inf

def tree_min_value(root):
  if root is None:
    return None

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

from math import inf

# recursive
def tree_min_value(root):
  if root is None:
    return +inf

  left_values = tree_min_value(root.left)
  right_values = tree_min_value(root.right)

  return min(root.val, left_values, right_values)
