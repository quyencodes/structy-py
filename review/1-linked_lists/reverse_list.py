# time - o(n)
# space - o(1)

def reverse_list(head):
  if head is None:
    return None

  if head.next is None:
    return head

  new_head = reverse_list(head.next)
  head.next.next = head
  head.next = None
  return new_head


# time - o(n)
# space - o(1)
# def reverse_list(head):
#   prev = None
#   current = head
#   while current:
#     saved_next = current.next
#     current.next = prev
#     prev = current
#     current = saved_next
#   return prev

# None <- a -> b -> c -> None
#                  prev
#                        curr

"""
saved_next = b

"""