# time - o(min(n, m)), n being the length of head_1 and m being the length of head_2
# space - o(1)

def zipper_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  current_1 = head_1
  current_2 = head_2
  count = 0
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
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




# def zipper_lists(head_1, head_2):
#   if head_1 is None and head_2 is None:
#     return None

#   if head_1 is None:
#     return head_2

#   if head_2 is None:
#     return head_1

#   saved_1 = head_1.next
#   saved_2 = head_2.next
#   head_1.next = head_2
#   head_2.next = zipper_lists(saved_1, saved_2)
#   return head_1


"""
a -> b -> c

x -> y -> z

"""
