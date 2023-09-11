class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_post(in_order, post_order):
  if len(in_order) == 0 and len(post_order) == 0:
    return None

  current = post_order[-1]
  root = Node(current)
  index = in_order.index(current)

  left_inorder = in_order[0:index]
  right_inorder = in_order[index + 1:]

  left_postorder = post_order[0:len(left_inorder)]
  right_postorder = post_order[len(left_inorder) : len(left_inorder) + len(right_inorder)]

  root.left = build_tree_in_post(left_inorder, left_postorder)
  root.right = build_tree_in_post(right_inorder, right_postorder)

  return root

# in_order = [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ]
# post_order = [ 'd', 'g', 'h', 'e', 'b', 'f', 'c', 'a' ]
# index = in_order.index('a')
# left_inorder = in_order[0:index]
# right_inorder = in_order[index+1:]
# left_postorder = post_order[0:len(left_inorder)]
# right_postorder = post_order[len(left_inorder): len(left_inorder) + len(right_inorder)]
# print(right_postorder)