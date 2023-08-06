class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def create_linked_list(values):
  dummy_head = Node(None)
  tail = dummy_head

  for value in values:
    tail.next = Node(value)
    tail = tail.next

  return dummy_head.next


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def create_linked_list(values):
  return _create_linked_list(values, 0)


def _create_linked_list(values, i):
  if i == len(values):
    return None

  new_head = Node(values[i])
  new_head.next = _create_linked_list(values, i + 1)
  return new_head
