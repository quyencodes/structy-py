def linked_list_values(head):
  values = []
  current = head
  while current:
    values.append(current.val)
    current = current.next
  return values
