def tree_min_value(root):
  if root is None:
    return float('+inf')

  return min(root.val, tree_min_value(root.left), tree_min_value(root.right))
