# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# time - o(n)
# space - o(1)
def get_node_value(head, index):
  count = 0
  current = head
  while current:
    if count == index:
      return current.val
    count += 1
    current = current.next

  return None

# time - o(n)
# space - o(1)
# def get_node_value(head, index):
#   if head is None:
#     return None

#   if index == 0:
#     return head.val

#   return get_node_value(head.next, index - 1)
