from collections import deque


def bottom_right_value(root):
  queue = deque([root])
  if root is None:
    return None

  while queue:
    curr = queue.popleft()

    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)

  return curr.val
