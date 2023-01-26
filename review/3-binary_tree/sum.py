def tree_sum(root):
  # empty binary tree
  if root is None:
    return 0

  # leaf
  if root.left is None and root.right is None:
    return root.val

  return root.val + tree_sum(root.left) + tree_sum(root.right)

from collections import deque
def tree_sum(root):
  if root is None: return 0
  sum = 0
  queue = [ root ]
  while len(queue) > 0:
    current = queue.pop(0)
    sum += current.val
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return sum