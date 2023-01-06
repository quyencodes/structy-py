class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

# iterative
def linked_list_values(head):
  if head is None:
    return []

  values = []
  current = head
  while current is not None:
    values.append(current.val)

    current = current.next

  return values


# recursive
def linked_list_values(head):
  values = []
  explore_values(head, values)
  return values

def explore_values(head, values):
  if head is None:
    return None

  values.append(head.val)
  explore_values(head.next, values)
