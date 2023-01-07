class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative
def sum_list(head):
  if head is None:
    return 0
  current = head
  sum = 0
  while current is not None:
    sum += current.val

    current = current.next

  return sum

# recursive
def sum_list(head):
  if head is None:
    return 0

  return head.val + sum_list(head.next)
