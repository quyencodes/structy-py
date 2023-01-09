def get_node_value(head, index):
  if head is None:
    return None

  if index == 0:
    return head.val

  return get_node_value(head.next, index - 1)

def get_node_value(head, index):
  if head is None:
    return None

  current = head
  while current is not None:
    if index == 0:
      return current.val

    index -= 1
    current = current.next

  reeturn None