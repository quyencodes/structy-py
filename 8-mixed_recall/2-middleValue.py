# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

"""
Brute force solution: Use a list, add all the nodes to the list, and grab the middle value by len(list) // 2.
Optimal solution: Use a slow and fast pointer. Fast will move 2x faster than slow. Iterate until fast and fast.next is not None. Return slow.val at the end.
"""


def middle_value(head):
  values = []
  curr = head

  while curr:
    values.append(curr.val)
    curr = curr.next

  return values[len(values) // 2]
