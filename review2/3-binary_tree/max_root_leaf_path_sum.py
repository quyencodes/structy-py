def max_path_sum(root):
  if root is None:
    return

  left_path = max_path_sum(root.left)
  right_path = max_path_sum(root.right)

  return max(root.val, left_path, right_path)


