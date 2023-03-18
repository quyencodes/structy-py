# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from statistics import mean
from collections import deque
def level_averages(root):
  if root is None: return []
  res = _level_averages(root)
  return [ mean(sublist) for sublist in res ]
#   averages = []
#   for sublist in res:
#     averages.append(mean(sublist))

#   return averages

def _level_averages(root):
  queue = deque([ (root, 0) ])
  levels = []
  while queue:
    current, level_num = queue.popleft()
    if len(levels) == level_num:
      levels.append([current.val])
    else:
      levels[level_num].append(current.val)

    if current.left: queue.append((current.left, level_num+1))
    if current.right: queue.append((current.right, level_num+1))

  return levels