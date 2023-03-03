def mergeTwoSortedLists(self, head_1, head_2):
  # if head_1 is None and head_2 is None: return None
  dummy_head = Node(None)
  tail, current_1, current_2 = dummy_head, head_1, head_2
  while current_1 is not None and current_2 is not None:
    if current_1.val <= current_2.val:
      tail.next, current_1 = current_1, current_1.next
    else:
      tail.next, current_2 = current_2, current_2.next

    tail = tail.next

  # work with leftover list
  if current_1 is None:
    tail.next = current_2
  if current_2 is None:
    tail.next = current_1

  return dummy_head.next

"""
list1 = 1 -> 3 -> None, list2 = 2 -> 4 -> None
dummy_head = None -> 1 -> 2 -> 3
tail.next = 3
current_1 = None
- saved_next = None
current_2 = 2

"""


  # def mergeTwoSortedLists(self, head_1, head_2):
  #   if head_1 is None and head_2 is None:
  #     return None

  #   if head_1 is None:
  #     return head_2

  #   if head_2 is None:
  #     return head_1

  #   if head_1.val <= head_2.val:
  #     saved_next = head_1.next
  #     head_1.next = self.mergeTwoSortedLists(saved_next, head_2)
  #     return head_1
  #   else:
  #     saved_next = head_2.next
  #     head_2.next = self.mergeTwoSortedLists(head_1, saved_next)
  #     return head_2