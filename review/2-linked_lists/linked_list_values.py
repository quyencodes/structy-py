class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# iterative solution
def linked_list_values(head):
  current = head
  values = []

  while current is not None:
    values.append(current.val)
    current = current.next

  return values


# recursive solution
def linked_list_values(head):
  values = []

  def valueshelper(current):
    if current is None:
      return None

    values.append(current.val)
    valueshelper(current.next)

  valueshelper(head)
  return values

  # a -> b -> c -> d

  # ['a', 'b', 'c', 'd']
