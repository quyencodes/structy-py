# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

"""
Use slow and fast pointers. Start at the same spot, fast will move 2x slow. Check after we change the pointers.
"""


def linked_list_cycle(head):
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow is fast:
      return True

  return False
