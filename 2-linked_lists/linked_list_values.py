class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# iterative approach
def linked_list_values(head):
  current = head
  ll_values = []
  while current is not None:
    ll_values.append(current.value)
    current = current.next

  return ll_values

# recursive approach
def linked_list_values(head):
  result = []
  # base case
  if head is None:
    return result

  result.append(head.value)

  # recursive case
  linked_list_values(head.next)

  return result


# recursive inner function approach
def linked_list_values(head):
  result = []

  def inner_function(current):
    if current is None:
      return

    result.append(current.val)
    inner_function(current.next)

  inner_function(head)
  return result