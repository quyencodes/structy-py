from collections import deque

# bfs
def tree_value_count(root, target):
  if root is None:
    return 0

  queue = deque([ root ])
  count = 0
  while queue:
    current = queue.popleft()

    if current.val == target:
      count += 1

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

  return count

# dfs
def tree_value_count(root, target):
  if root is None:
    return 0

  stack = deque([ root ])
  count = 0
  while stack:
    current = stack.pop()

    if current.val == target:
      count += 1

    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return count

# recursive
def tree_value_count(root, target):
  if root is None:
    return 0

  match = 1 if root.val == target else 0

  return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)