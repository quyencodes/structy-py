def tree_sum(root):
  if root is None:
    return 0

  return root.val + tree_sum(root.left) + tree_sum(root.right)

import collections

def tree_sum(root):
  if root is None: return 0
  total, queue = 0, collections.deque([root])

  while queue:
    current = queue.popleft()
    total += current.val

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return total