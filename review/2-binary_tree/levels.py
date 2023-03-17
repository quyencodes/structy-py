def tree_levels(root, levels=[], level_num=0):
  if root is None:
    return []

  if len(levels) == level_num:
    levels.append([root.val])
  else:
    levels[level_num].append(root.val)

  tree_levels(root.left, levels, level_num+1)
  tree_levels(root.right, levels, level_num+1)
  return levels