from math import inf
from collections import deque

def tree_min_value(root):
  if root is None:
    return +inf

  left_values = tree_min_value(root.left)
  right_values = tree_min_value(root.right)

  return min(root.val, left_values, right_values)

#     a
#    / \
#   b   c
#  / \   \
# d   e   f

# return min(3, -2, 1)
# left_values = -2
# right_values = 1

# return min(11, 4, -2)
# root.val = 11
# left_values = 4
# right_values = -2

# return min(4, +inf, +inf)
# root.val = 4
# left_values = +inf
# right_values = +inf
