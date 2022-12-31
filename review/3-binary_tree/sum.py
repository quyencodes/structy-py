from collections import deque

def tree_sum(root):
  if root is None:
    return 0

  total_sum = 0
  queue = deque([root])
  while queue:
    current = queue.popleft()
    total_sum += current.val

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return total_sum
