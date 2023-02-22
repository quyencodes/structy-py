# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque
def flip_tree(root):
  if root is None: return None
  queue = deque([root])
  while queue:
    current = queue.popleft()
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

    current.left, current.right = current.right, current.left

  return root

#   if root is None:
#     return None

#   root.left, root.right = flip_tree(root.right), flip_tree(root.left)
#   return root