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

def reverse_list(head):
  prev = None
  current = head

  while current is not None:
    next = current.next
    # logic here
    current.next = prev

    prev = current
    current = next

  return prev