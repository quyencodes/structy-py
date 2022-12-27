def tree_count(root, target):
  if root is None:
    return 0

  return match + tree_count(root.left, target) + tree_count(root.right, target)

from collections import deque

def tree_count(root, target):
  if root is None:
    return 0

  count = 0
  queue = deque([ root ])

  while queue:
    current = queue.popleft()

    if current.val == target:
      count += 1

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return count