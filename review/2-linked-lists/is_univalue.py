# time - o(n), space - o(1)
def is_univalue_list(head):
  current = head
  while current:
    if current.val != head.val:
      return False
    current = current.next

  return True

# 7 -> 7 -> 7 -> None
# time - o(n), space - o(n)
def is_univalue_list(head, prev = None):
  if head is None:
    return True

  if prev is None or head.val == prev:
    return is_univalue_list(head.next, head.val)
  else:
    return False
