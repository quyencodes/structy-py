class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_post(in_order, post_order):
  if len(in_order) == 0: # checks post lists because they are same length
    return None

  val = post_order[-1]
  root = Node(val)
  mid = in_order.index(val)
  left_in_order = in_order[:mid]
  right_in_order = in_order[mid+1:]

  left_post_order = post_order[:len(left_in_order)]
  right_post_order = post_order[len(left_in_order): -1]

  root.left = build_tree_in_post(left_in_order, left_post_order)
  root.right = build_tree_in_post(right_in_order, right_post_order)

  return root

