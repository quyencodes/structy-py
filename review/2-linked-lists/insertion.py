# time - o(n), space - o(n)

def insert_node(head, value, index):
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head

  if index == 1:
    new_node = Node(value)
    saved_next = head.next
    head.next = new_node
    new_node.next = saved_next
    return

  insertion = insert_node(head.next, value, index - 1)
  return head