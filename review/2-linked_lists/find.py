class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

def linked_list_find(head, target):
  if head is None:
    return False

  if head.val == target:
    return True

  return linked_list_find(head.next, target)