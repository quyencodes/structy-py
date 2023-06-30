# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def binary_search_tree_includes(root, target):
  if root is None:
    return False

  if root.val == target:
    return True

  if target < root.val:
    attempt = binary_search_tree_includes(root.left, target)
  elif target > root.val:
    attempt = binary_search_tree_includes(root.right, target)

  return True if attempt == True else False

def binary_search_tree_includes(root, target):
  if root is None:
    return False

  if root.val == target:
    return True

  if target < root.val:
    return binary_search_tree_includes(root.left, target)
  elif target > root.val:
    return binary_search_tree_includes(root.right, target)


