def linked_list_cycle(head):
  visited = set()
  return _linked_list_cycle(head, visited)

def _linked_list_cycle(head, visited):
  if head is None:
    return False

  if head.val in visited:
    return True

  visited.add(head.val)
  return _linked_list_cycle(head.next, visited)

def linked_list_cycle(head):
  slow = head
  fast = head
  start = True
  while not (fast is None or fast.next is None):
    if slow.val == fast.val and not start:
      return True

    slow = slow.next
    fast = fast.next.next
    start = False

  return False