def linked_list_find(head, target):
  if head is None:
    return False

  if head.val == target:
    return True

  return linked_list_find(head.next, target)


def linked_list_find(head, target):
  curr = head

  while curr is not None:
    if curr.val == target:
      return True
    curr = curr.next

  return False
