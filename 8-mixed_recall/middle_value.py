# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def middle_value(head):
  mid = head
  fast = head

  while mid is not None and fast is not None:
    if fast is None or fast.next is None:
      return mid.val
    mid = mid.next
    fast = fast.next.next

  return mid.val
