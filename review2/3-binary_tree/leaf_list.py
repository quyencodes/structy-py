def leaf_list(root):

  leaves = []

  def leafhelper(root):
    if root is None:
      return

    if root.left is None and root.right is None:
      leaves.append(root.val)

    leafhelper(root.left)
    leafhelper(root.right)

  leafhelper(root)
  return leaves
