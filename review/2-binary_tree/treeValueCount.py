def tree_value_count(root, target):
  if root is None:
    return 0

  count = 1 if root.val == target else 0

  count += tree_value_count(root.left, target)
  count += tree_value_count(root.right, target)

  return count

def how_high(node):
  res = _how_high(node)
  if res == -1:
    return -1
  else:
    return len(_how_high(node)) - 1

#   if node is None:
#     return -1

#   return 1 + max(how_high(node.left), how_high(node.right))

from collections import deque
def _how_high(root):
  if root is None: return -1
  queue = deque([(root, 0)])
  levels = []
  while queue:
    current, level_num = queue.popleft()

    if len(levels) == level_num:
      levels.append([current.val])
    else:
      levels[level_num].append(current.val)

    if current.left: queue.append((current.left, level_num + 1))
    if current.right: queue.append((current.right, level_num + 1))

  return levels
