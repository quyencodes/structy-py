class Node:
  def __init__(self, value):
    self.value = value
    self.next = next

# iterative approach
def sum_list(head):
  current = head
  sum = 0

  while current is not None:
    sum += current.val
    current = current.next

  return sum

# recursive approach
def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)