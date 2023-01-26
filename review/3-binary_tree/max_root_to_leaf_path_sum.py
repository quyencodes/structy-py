def max_path_sum(root):
  if root is None:
    return float("-inf")

  if root.left is None and root.right is None:
    return root.val

  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


#     8
#    / \
#   4   10
#  / \   \
# 2   3   -1
#      \
#       15

# 8 + 4 + 2 = 14
# 8 + 4 + 3 + 15 = 30
# 8 + 10 - 1 = 17

# mps(4) return 4 + max(2, 18)
# mps(3) return 3 + max(15)
# mps(15) return 15