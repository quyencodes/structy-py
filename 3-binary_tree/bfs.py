# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque


def breadth_first_values(root):
  res, queue = [], deque([root])
  if root is None:
    return res

  while queue:
    curr = queue.popleft()
    res.append(curr.val)

    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)

  return res
