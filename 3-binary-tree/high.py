def how_high(root):
  if root is None:
    return -1

  right_tree_height = how_high(root.right)

  return 1 + max(right_tree_height)