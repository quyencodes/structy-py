# input - two heads of a linked list
# output - a single linked list of them sorted by their values
# constraints - none
# edge cases - none

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# n - len(head_1), m - len(head_2)
# time - o(min(n, m))
# space - o(1)
# iterative
def merge_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  current_1 = head_1
  current_2 = head_2
  while current_1 is not None and current_2 is not None:
    if current_1.val < current_2.val:
      tail.next = current_1
      current_1 = current_1.next
    else:
      tail.next = current_2
      current_2 = current_2.next

    tail = tail.next

  if current_1 is None:
    tail.next = current_2
  if current_2 is None:
    tail.next = current_1

  return dummy_head.next

# time - o(min(n, m))
# space - o(min(n, m))

# recursive
def merge_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None

  if head_1 is None:
    return head_2

  if head_2 is None:
    return head_1

  if head_1.val < head_2.val:
    next_1 = head_1.next
    head_1.next = merge_lists(next_1, head_2)
    return head_1
  else:
    next_2 = head_2.next
    head_2.next = merge_lists(head_1, next_2)
    return head_2

# 5 -> None
# 2 -> 3 -> 5 -> None


#   5 -> 7 -> 12 -> 28 -> None
#                 curr_1
#   6 -> 9 -> 15 -> 20 -> None
#                        curr_2

# actual
# None -> 5 -> 6 -> 7 -> 9 -> 12 -> 15 -> 20 -> 28 -> None
#                                   tail

# expected
# 5 -> 6 -> 7 -> 9 -> 12 -> 15 -> 20 -> 28 -> None