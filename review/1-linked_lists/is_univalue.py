def is_univalue_list(head):
  prev = None
  current = head
  while current is not None:
    if prev is not None and prev.val != current.val:
      return False
    prev = current
    current = current.nextis
  return True