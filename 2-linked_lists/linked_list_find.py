class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# iterative approach
def linked_list_find(head, target):
  current = head

  while current is not None:
    if current.val == target:
      return True

    current = current.next

  return False

# wrapper recursive approach
def linked_list_find(head, target):

  def findhelper(current):
    if current is None:
      return False


    if current.val == target:
      return True

    findhelper(current.next)

  return findhelper(head)

# pure recursion approach
def linked_list_find(head, target):
  # base case
  if head is None:
    return False
  if head.val == target:
    return True

  # recursive case
  return linked_list_find(head.next, target)