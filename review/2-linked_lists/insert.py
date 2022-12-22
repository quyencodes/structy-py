def insert_node(head, value, index):
  if index == 0:
    new_node = Node(value)
    new_node.next = head
    return new_node

  if head is None:
    return None

  # head.next = new_node
  # new_node.next = the rest
  head.next = insert_node(head.next, value, index - 1)
  return head

def insert_node(head, value, index):
  prev = None
  current = head

  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head

  while current is not None:

    index -= 1

    if index == 0:
      saved_node = current.next
      new_node = Node(value)
      current.next = new_node
      new_node.next = saved_node
      break

    prev = current
    current = current.next

  return head