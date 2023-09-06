def lefty_nodes(root):
  res = []
  _lefty_nodes(root, res, 0)
  return res

def _lefty_nodes(root, nodes, level):
  if root is None:
    return

  if len(nodes) == level:
    nodes.append(root.val)

  _lefty_nodes(root.left, nodes, level+1)
  _lefty_nodes(root.right, nodes, level+1)

  return

from collections import deque
def lefty_nodes(root):
  levels = []
  level_num = 0
  if root is None: return []
  queue = deque([(root, level_num)])

  while queue:
    current, level = queue.popleft()

    if len(levels) == level:
      levels.append([current.val])
    else:
      levels[level].append(current.val)

    if current.left is not None:
      queue.append((current.left, level+1))
    if current.right is not None:
      queue.append((current.right, level+1))

  res = []
  for level in levels:
    res.append(level[0])

  return res