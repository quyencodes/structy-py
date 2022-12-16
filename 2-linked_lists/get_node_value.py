def get_node_value(head, index):
  # iterative approach
  current = head
  index_tracker = 0

  while current is not None:
    if index_tracker == index:
      return current.val

    current = current.next
    index_tracker += 1

  return None

# recursive approach
def get_node_value(head, index):
  # base case
  if head is None:
    return None

  # head.val, head.next, index
  if index == 0:
    return head.val

  # recursive case
  return get_node_value(head.next, index-1)

# wrapper function recursive function
def get_node_value(head, index):
  # base case
  if head is None or index < 0:
    return None

  # head.val, head.next, index
  if index == 0:
    return head.val

  # recursive case
  return get_node_value(head.next, index-1)