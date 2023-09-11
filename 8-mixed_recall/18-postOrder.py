# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

"""
post-order: left, right, self
"""

def post_order(root):
  values = []
  post_order_traversal(root, values)
  return values

def post_order_traversal(root, values):
  if root is None:
    return

  post_order_traversal(root.left, values)
  post_order_traversal(root.right, values)
  values.append(root.val)
  return

