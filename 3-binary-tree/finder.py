def path_helper(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  else:
    return result[::-1]

def _path_finder(root, target):
  if root is None:
    return None

  if root.val == target:
    return [root.val]

  left_values = path_finder(root.left, target)
  right_values = path_finder(root.right, target)

  if left_values is not None:
    left_values.append(root.val)
    return left_values
  if right_values is not None:
    right_values.append(root.val)
    return right_values

