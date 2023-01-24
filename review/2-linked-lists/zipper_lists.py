# input - 2 heads of linked lists
# output - new head of the zippered linked list
# constraints - none
# edge cases - none

# n - len(head_1), m - len(head_2)
# time - o(min(n,m))
# space - o(1)
def zipper_lists(head_1, head_2):
  tail = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      tail.next = current_2
      current_2 = current_2.next
    else:
      tail.next = current_1
      current_1 = current_1.next

    tail = tail.next
    count += 1

  if current_1 is None:
    tail.next = current_2
  if current_2 is None:
    tail.next = current_1

  return head_1

# tail
#   a -> b -> c -> None (odd)
#       curr
#   x -> y -> z -> None (even)
#       curr

# actual
# a -> x -> b -> y -> c -> z

# expected
# a -> x -> b -> y -> c -> z -> None

# time - o(n)
# space - o(n)
def zipper_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None

  if head_1 is None:
    return head_2

  if head_2 is None:
    return head_1

  next_1 = head_1.next
  next_2 = head_2.next
  head_1.next = head_2
  head_2.next = zipper_lists(next_1, next_2)
  return head_1
