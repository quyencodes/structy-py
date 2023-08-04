def remove_node(head, target_val):
  if head is None:
    return None

  if head.next is None:
    return None

  if head.val == target_val:
    return head.next

  if head.next.val == target_val:
    head.next = head.next.next
    return head

  remove_node(head.next, target_val)
  return head


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):
  if head.val == target_val:
    return head.next

  prev = None
  curr = head

  while curr:
    if curr.val == target_val:
      prev.next = curr.next
      return head

    prev = curr
    curr = curr.next

  return head
