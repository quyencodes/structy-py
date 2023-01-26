def tree_min_value(root):
  if root is None:
    return float("+inf")

  left_values = tree_min_value(root.left) # int
  right_values = tree_min_value(root.right) # int

  return min(root.val, left_values, right_values)

# iterative
def tree_min_value(root):
  min_value = float("+inf")
  queue = [ root ]
  while queue:
    current = queue.pop(0)
    if current.val < min_value:
      min_value = current.val

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return min_value

#     5
#    / \
#   2   4
#  / \   \
# -1  3   6
# + inf
