def tree_levels(root):
  levels = []
  def levelshelper(root, level_num = 0):
    if root is None:
      return []

    if len(levels) == level_num:
      levels.append([root.val])
    else:
      levels[level_num].append(root.val)

    levelshelper(root.left, level_num + 1)
    levelshelper(root.right, level_num + 1)

  levelshelper(root)
  return levels