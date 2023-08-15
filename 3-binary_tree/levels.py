from collections import deque


def tree_levels(root):
  if root is None:
    return []

  levels, queue = [], deque([(root, 0)])

  while queue:
    curr, level_num = queue.popleft()

    if len(levels) == level_num:
      levels.append([curr.val])
    else:
      levels[level_num].append(curr.val)

    if curr.left:
      queue.append((curr.left, level_num + 1))
    if curr.right:
      queue.append((curr.right, level_num + 1))

  return levels
