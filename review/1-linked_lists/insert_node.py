def insert_node(head, value, index):
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head

  head.next = insert_node(head.next, value, index-1)
  return head