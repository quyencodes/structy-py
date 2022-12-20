class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# iterative approach
def remove_node(head, target_val):
  current = head
  prev = None

  if current.val == target_val:
    return current.next

  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      break

    prev = current
    current = current.next

  return head

# recursive solution
def remove_node(head, target_val):
  if head is None:
    return None

  if head.val == target_val:
    return head.next

  head.next = remove_node(head.next, target_val)

  return head
