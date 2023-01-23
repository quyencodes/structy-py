# time - o(n)
# space - o(1)

def linked_list_find(head, target):
  current = head
  while current:
    if current.val == target:
      return True
    current = current.next
  return False

# time - o(n)
# space - o(n)
def linked_list_find(head, target):
  if head is None:
    return False

  if head.val == target:
    return True

  return linked_list_find(head.next, target)