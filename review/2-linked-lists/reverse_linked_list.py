# input - head of the linked list
# output - reverse the linked list and return the new head
# constraints - none
# edge cases - none

# time - o(n)
# space - o(1)

# iterative
def reverse_list(head):
  prev = None
  current = head
  while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

# None <- a <- b <- c -> None
#                  prev curr
# None <- a <- b <- c

# time - o(n)
# space - o(n)

# recursive
def reverse_list(head):
  if head is None:
    return None

  if head.next is None:
    return head

  new_head = reverse_list(head.next)
  head.next.next = head
  head.next = None
  return new_head