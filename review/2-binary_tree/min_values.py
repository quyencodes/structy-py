def tree_min_value(root):
  if root is None:
    return float("+inf")

  return min(root.val, tree_min_value(root.left), tree_min_value(root.right))

from collections import deque
import math
def tree_min_value(root):
  queue = deque([root])
  res = float("inf")
  while queue:
    current = queue.popleft()
    res = min(current.val, res)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return res
