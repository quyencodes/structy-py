

# time - o(min(n, m)) n being the length of list 1 and m being the length of list 2
# space - o(min(n, m))
def merge_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None

  if head_1 is None:
    return head_2

  if head_2 is None:
    return head_1

  if head_1.val < head_2.val:
    saved_1 = head_1.next
    head_1.next = merge_lists(saved_1, head_2)
    return head_1
  else:
    saved_2 = head_2.next
    head_2.next = merge_lists(head_1, saved_2)
    return head_2