class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  if len(values) == 0:
    return None

  # create a node
  head = Node(values[0])

  # head.next = next_node
  head.next = create_linked_list(values[1:])

  return head

def create_linked_list(values):
  dummy_head = Node(None)
  tail = dummy_head

  for value in values:
    new_node = Node(value)
    tail.next = new_node
    tail = tail.next

  return dummy_head.next