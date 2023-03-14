def create_linked_list(values):
  return _create_linked_list(values, 0)

def _create_linked_list(values, index):
  if index == len(values):
    return None
  new_head = Node(values[index])
  new_head.next = _create_linked_list(values, index+1)
  return new_head

def create_linked_list(values):
  dummy_head = Node(None)
  tail = dummy_head
  for val in values:
    new_node = Node(val)
    tail.next = new_node
    tail = tail.next

  return dummy_head.next
