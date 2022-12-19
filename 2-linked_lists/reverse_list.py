class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# iterative approach
def reverse_list(head):
  prev = None
  current = head

  while current is not None:
    # save next node
    next = current.next
    # reverse in place
    current.next = prev
    prev = current
    current = next

  return prev

# recursive approach
def reverse_list(head, prev = None):
  if head is None:
    return prev

  next = head.next

  head.next = prev

  reverse_list(next, head)