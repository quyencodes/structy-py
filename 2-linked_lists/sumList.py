def sum_list(head):
  if head is None:
    return 0

  return head.val + sum_list(head.next)


def sum_list(head):
  res = 0
  curr = head
  while curr is not None:
    res += curr.val
    curr = curr.next

  return res
