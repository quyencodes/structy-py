def tree_sum(root):
  if root is None:
    return 0

  left_sum = tree_sum(root.left)
  right_sum = tree_sum(root.right)

  return root.val + left_sum + right_sum



#     a
#    / \
#   b   c
#  / \   \
# d   e   f