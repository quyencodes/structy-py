class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre(in_order, pre_order):
  if len(in_order) == 0 and len(pre_order) == 0:
    return None

  current = pre_order[0]
  root = Node(current)
  index = in_order.index(current)

  left_inorder = in_order[0:index]
  right_inorder = in_order[index+1:]

  left_preorder = pre_order[1:len(left_inorder) + 1]
  right_preorder = pre_order[len(left_inorder) + 1:]

  root.left = build_tree_in_pre(left_inorder, left_preorder)
  root.right = build_tree_in_pre(right_inorder, right_preorder)

  return root