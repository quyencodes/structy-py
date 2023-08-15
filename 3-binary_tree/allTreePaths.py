def all_tree_paths(root):
  if root is None:
    return []

  if root.left is None and root.right is None:
    return [[root.val]]

  all_paths = []
  left_paths = all_tree_paths(root.left)
  for sublist in left_paths:
    temp = [root.val] + sublist
    all_paths.append(temp)

  right_paths = all_tree_paths(root.right)
  for sublist in right_paths:
    temp = [root.val] + sublist
    all_paths.append(temp)

  return all_paths
