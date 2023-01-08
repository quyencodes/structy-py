def linked_list_find(head, target):
  if head is None:
    return False

  if head.val == target:
    return True

  return linked_list_find(head.next, target)

def linked_list_find(head, target):
  if head is None:
    return False

  current = head
  while current is not None:
    if current.val == target:
      return True

    current = current.next

  return False