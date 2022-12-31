# bfs

# from collections import deque
def bottom_right_value(root):
  if root is None:
    return None

  queue = [ root ]
  while queue:
    current = queue.pop(0)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return current.val