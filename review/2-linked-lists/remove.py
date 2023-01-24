# input - head, target value
# output - return the head of the linked list with the remove node
def remove_node(head, target_val):
  if head is None:
    return None

  if head.val == target_val:
    return head.next

  head.next = remove_node(head.next, target_val)
  return head

# iterative
def remove_node(head, target_val):
  if head.val == target_val:
    return head.next

  current = head
  prev = None

  while current:
    if current.val == target_val:
      prev.next = current.next
      break
    prev = current
    current = current.next
  return head

# q -> r -> s -> None