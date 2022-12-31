from collections import deque
# bfs
def tree_levels(root):
  if root is None:
    return []

  levels = []
  queue = deque([ (root, 0) ])
  while queue:
    current, level = queue.popleft()

    if len(levels) == level:
      levels.append([current.val])
    else:
      levels[level].append(current.val)


    if current.left:
      queue.append((current.left, level + 1))
    if current.right:
      queue.append((current.right, level + 1))

  return levels

# recursive
def tree_levels(root):
  levels = []

  def levelshelper(root, level_num = 0):
    if root is None:
      return []

    if len(levels) == level_num:
      levels.append(root.val)
    else:
      levels[level_num].append(root.val)

    levelshelper(root.left, level_num + 1)
    levelshelper(root.right, level_num + 1)

  levelshelper(root)
  return levels