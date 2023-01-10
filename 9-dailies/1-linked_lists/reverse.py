def reverse_list(head):
  if head is None:
    return None

  if head.next is None:
    return head

  last_node = reverse_list(head.next)
  head.next.next = head
  head.next = None
  return last_node

def reverse_list(head):
  if head is None:
    return None

  current = head
  prev = None
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next

  return prev