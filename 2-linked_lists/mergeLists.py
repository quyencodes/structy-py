class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def merge_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  curr_1 = head_1
  curr_2 = head_2

  while curr_1 and curr_2:
    if curr_1.val <= curr_2.val:
      tail.next = curr_1
      curr_1 = curr_1.next
    else:
      tail.next = curr_2
      curr_2 = curr_2.next

    tail = tail.next

  if curr_1 is None:
    tail.next = curr_2
  if curr_2 is None:
    tail.next = curr_1

  return dummy_head.next
