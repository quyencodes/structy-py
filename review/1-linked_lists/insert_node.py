def insert_node(head, value, index):
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head

  head.next = insert_node(head.next, value, index-1)
  return head

def insert_node(head, value, index):
  dummy_head = Node(None)
  tail = dummy_head
  current = head

  while current is not None:
    if index == 0:
      new_node = Node(value)
      new_node.next = current
      tail.next = new_node
      return dummy_head.next

    index -= 1
    tail.next = current
    tail = tail.next
    current = current.next

  if index == 0:
    tail.next = Node(value)

  return dummy_head.next