def leaf_list(root):
  if root is None:
    return []

  stack = [ root ]
  leaves = []

  while stack:
    current = stack.pop()

    if current.left is None and current.right is None:
      leaves.append(current.val)

    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return leaves

def leaf_list(root):
  leaves = []
  def leafhelper(root):
    if root is None:
      return []

    if root.left is None and root.right is None:
      leaves.append(root.val)

    leafhelper(root.left)
    leafhelper(root.right)

  leafhelper(root)
  return leaves