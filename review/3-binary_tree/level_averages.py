# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from statistics import mean
def level_averages(root):
  level_list = _level_averages(root)
  averages = []
  for level in level_list:
    averages.append(mean(level))
  return averages

def _level_averages(root, levels=[], level=0):
  if root is None:
    return []

  if len(levels) == level:
    levels.append([root.val])
  else:
    levels[level].append(root.val)

  _level_averages(root.left, levels, level + 1)
  _level_averages(root.right, levels, level + 1)

  return levels
