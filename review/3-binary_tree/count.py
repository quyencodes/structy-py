#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12


def tree_value_count(root, target):
  if root is None:
    return 0

  match = 1 if root.val == target else 0

  return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)