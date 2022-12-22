class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head):
  if head.next is None:
    return True

  if head.val == head.next.val:
    return is_univalue_list(head.next)
  else:
    return False


def is_univalue_list(head):
  value = head.val
  current = head

  while current is not None:
    if value != current.val:
      return False

    current = current.next

  return True