# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_palindrome(head):
  values = traverse_nodes(head)
  return values == values[::-1]


def traverse_nodes(head):
  if head is None:
    return []
  curr = head
  values = []
  while curr:
    values.append(curr.val)
    curr = curr.next
  return values
