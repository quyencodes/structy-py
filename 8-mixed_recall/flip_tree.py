def flip_tree(root):
  if root is None:
    return None

  left_side = flip_tree(root.left)
  right_side = flip_tree(root.right)

  root.left = right_side
  root.right = left_side
  return root