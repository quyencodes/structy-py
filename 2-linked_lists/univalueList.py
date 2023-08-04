def is_univalue_list(head):
  prev = None
  curr = head

  while curr:
    if prev is not None and prev.val != curr.val:
      return False

    prev = curr
    curr = curr.next

  return True
