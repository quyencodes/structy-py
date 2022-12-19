class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# recursive way
def is_univalue_list(head, prev_val = None):
  if head is None:
    return True

  if prev_val is not None and prev_val != head.val:
    return False

  return is_univalue_list(head.next, head.val)