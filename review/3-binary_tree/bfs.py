from collections import deque

def depth_first_values(root):
  if root is None:
    return []

  values = []
  queue = deque([root])
  while queue:
    current = queue.popleft()
    values.append(current.val)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return values