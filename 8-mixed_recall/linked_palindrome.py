def linked_palindrome(head):
  # reverse the linked list
  rev_head = reverse_linkedlist(head)
  # check each node one by one
  return check_palindrome(head, rev_head)

def check_palindrome(head_1, head_2):
  if head_1 is None and head_2 is None:
    return True

  if head_1.val != head_2.val:
    return False

  return check_palindrome(head_1.next, head_2.next)

def reverse_linkedlist(head):
  prev = None
  current = head
  while current:
    saved_next = current.next
    current.next = prev
    prev = current
    current = saved_next

  return prev

# None <- a -> b -> c -> None
#         p    c
# sn = b

def reverse_linkedlist(head):
  if head is None:
    return None

  if head.next is None:
    return head

  new_head = reverse_linkedlist(head.next)
  new_head.next.next = head
  head.next = None
  return new_head
