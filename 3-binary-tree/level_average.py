from statistics import mean

def level_averages(root):

  levels = []

  def levelhelper(root, level_num):
    if root is None:
      return []

    if len(levels) == level_num:
      levels.append = [ root.val ]
    else:
      levels[level_num].append(root.val)

    levelhelper(root.left, level_num + 1)
    levelhelper(root.right, level_num + 1)

  levelhelper(root, 0)

  return [mean(level) for level in levels]