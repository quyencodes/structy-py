from collections import deque


def tree_sum(root):
  res, queue = 0, deque([root])
  if root is None:
    return res
  while queue:
    curr = queue.popleft()
    res += curr.val

    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)

  return res


def tree_sum(root):
  if root is None:
    return 0

  return root.val + tree_sum(root.left) + tree_sum(root.right)
