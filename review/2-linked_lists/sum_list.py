class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# iterative solution
def sum_list(head):
  total = 0
  current = head

  while current is not None:
    total += current.val
    current = current.next

  return total

# recursive solution
def sum_list(head):
  if head is None:
    return 0

  return head.val + sum_list(head.next)



