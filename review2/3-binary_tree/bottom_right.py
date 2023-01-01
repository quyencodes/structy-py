from collections import deque

def bottom_right_value(root):
  if root is None:
    return None

  queue = deque([root])
  while queue:
    current = queue.popleft()

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return current.val
