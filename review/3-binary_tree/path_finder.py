#     a
#    / \
#   b   c
#  / \   \
# d   e   f

# path_finder(a, 'e') -> ['a', 'b', 'e']

#     a
#    / \
#   b   c
#  / \   \
# d   e   f

# path_finder(a, 'p') -> None


def path_finder(root, target):
  # path finding algorithm
  path = []
  find_node(root, target)
  return reverse_list(path)
  # reverse my list

def find_node(root, target):
  if root is None:
    return []

  if root.val == target:
    return [root.val]

  if len(find_node(root.left, target)) > 0:
    return [root.val] + find_node(root.left, target)
  if len(find_node(root.left, target)) > 0:
    return [root.val] + find_node(root.right, target)

  return []

def reverse_list(list):
  if len(list) > 0:
    return list[::-1]
  else:
    return None