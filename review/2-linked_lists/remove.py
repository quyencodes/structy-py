def remove_node(head, target_val):
  if head is None:
    return None

  if head.val == target_val:
    return head.next

  # head.next = head.next.next
  head.next = remove_node(head.next, target_val)

  # return head
  return head

def remove_node(head, target_val):
  prev = None
  current = head

  if head.val == target_val:
    return head.next

  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      break

    prev = current
    current = current.next

  return head