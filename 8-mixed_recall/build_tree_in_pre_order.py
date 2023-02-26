class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre(in_order, pre_order):
  return _build_tree_in_pre(in_order, pre_order, 0, len(in_order)-1, 0, len(pre_order)-1)

def _build_tree_in_pre(in_order, pre_order, start_in, end_in, start_pre, end_pre):
  if end_in < start_in:
    return None

  value = pre_order[start_pre]
  root = Node(value)
  mid = in_order.index(value)
  left_size = mid - start_in
  root.left = _build_tree_in_pre(in_order, pre_order, start_in, mid - 1, start_pre + 1, start_pre + left_size)
  root.right = _build_tree_in_pre(in_order, pre_order, mid + 1, end_in, start_pre + left_size + 1, end_pre)
  return root

print(build_tree_in_pre(
  [ 'z', 'y', 'x' ],
  [ 'y', 'z', 'x' ]
))
#       y
#    /    \
#   z      x



class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre(in_order, pre_order):
  if len(in_order) == 0:
    return None

  val = pre_order[0]
  root = Node(val)

  mid = in_order.index(val)
  left_in_order = in_order[:mid]
  right_in_order = in_order[mid+1:]

  left_pre_order = pre_order[1:len(left_in_order)+1]
  right_pre_order = pre_order[len(left_in_order)+1:]

  root.left = build_tree_in_pre(left_in_order, left_pre_order)
  root.right = build_tree_in_pre(right_in_order, right_pre_order)

  return root

print(build_tree_in_pre(
  [ 'z', 'y', 'x' ],
  [ 'y', 'z', 'x' ]
))
#       y
#    /    \
#   z      x