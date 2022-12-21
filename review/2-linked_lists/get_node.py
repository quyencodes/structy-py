class Node:
  def __init__(self, values):
    self.value = values
    self.next = None

def get_node_value(head, index):
  if head is None:
    return None

  if index == 0:
    return head.val

  return get_node_value(head.next, index - 1)