def leaf_list(root):
  if root is None:
    return []

  if root.left is None and root.right is None:
    return [ root.val ]

  left_leaves = leaf_list(root.left) # ['d', 'e']
  right_leaves = leaf_list(root.right) # ['f']

  leaves = []
  for leaf in left_leaves:
    leaves.append(leaf)

  for leaf in right_leaves:
    leaves.append(leaf)

  return leaves

def leaf_list(root, leaves = []):
  if root is None:
    return []

  if root.left is None and root.right is None:
    leaves.append(root.val)

  left_leaves = leaf_list(root.left, leaves) # ['d', 'e']
  right_leaves = leaf_list(root.right, leaves) # ['f']

  return leaves

#      a
#     / \
#    b   c
#   / \   \
#  d   e   f
