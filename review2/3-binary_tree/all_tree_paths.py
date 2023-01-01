def all_tree_paths(root):
  if root is None:
    return []

  if root.left is None and root.right is None:
    return [[root.val]]

  paths = []

  left_path = all_tree_paths(root.left)
  for subpath in left_path:
    paths.append([root.val, *subpath])

  right_path = all_tree_paths(root.right)
  for subpath in right_path:
    paths.append([root.val, *subpath])

  return paths