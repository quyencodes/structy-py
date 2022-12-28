def tree_levels(root):
  if root is None:
    return []

  levels = []
  stack = [(root, 0)]

  while stack:
    node, level_num = stack.pop()

    if len(levels) == level_num:
      levels.append([ node.val ])
    else:
      levels[level_num].append(node.val)

    if node.right:
      stack.append((node.right, level_num + 1))
    if node.left:
      stack.append((node.left, level_num + 1))

  return levels

from collections import deque

def tree_levels(root):
  if root is None:
    return []

  levels = []
  queue = deque([(root, 0)])

  while queue:
    node, level_num = queue.popleft()

    if len(levels) == level_num:
      levels.append([ node.val ])
    else:
      levels[level_num].append(node.val)

    if node.left:
      queue.append((node.left, level_num + 1))
    if node.right:
      queue.append((node.right, level_num + 1))

  return levels

# recursive solution
def tree_levels(root):
  levels = []
  def levelshelper(root, level_num):
    nonlocal levels

    if root is None:
      return

    if len(levels) == level_num:
      levels.append([ root.val ])
    else:
      levels[level_num].append(root.val)

    levelshelper(root.left, level_num + 1)
    levelshelper(root.right, level_num + 1)

  levelshelper(root, 0)
  return levels