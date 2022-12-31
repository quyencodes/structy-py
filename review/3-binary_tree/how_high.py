# recursive
def how_high(node):
  if node is None:
    return -1

  left_path = how_high(node.left)
  right_path = how_high(node.right)

  return 1 + max(left_path, right_path)