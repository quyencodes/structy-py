def linked_list_values(head):
  if head is None:
    return []

  values = linked_list_values(head.next)
  return [head.val, *values]


def linked_list_values(head):
  values = []

  curr = head

  while curr is not None:
    values.append(curr.val)
    curr = curr.next

  return values
