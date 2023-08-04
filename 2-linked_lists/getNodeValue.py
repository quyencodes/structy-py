def get_node_value(head, index):
  curr = head

  while curr is not None:
    if index == 0:
      return curr.val

    index -= 1
    curr = curr.next

  return None


def get_node_value(head, index):
  if head is None:
    return None

  if index == 0:
    return head.val

  return get_node_value(head.next, index - 1)
