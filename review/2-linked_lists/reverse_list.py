class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

def reverse_list(head):
  if head is None:
    return None

  if head.next is None:
    return head

  next_node = reverse_list(head.next)
  head.next.next = head
  # change head's next to None
  head.next = None
  return next_node