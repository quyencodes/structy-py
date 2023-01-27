def how_high(node):
  if node is None:
    return -1

  if node.left is None and node.right is None:
    return 0

  return 1 + max(how_high(node.left), how_high(node.right))