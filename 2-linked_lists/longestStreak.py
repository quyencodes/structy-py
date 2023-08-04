def longest_streak(head):
  prev = None
  curr = head
  curr_count = 0
  max_count = 0

  while curr is not None:
    if prev is None or prev.val == curr.val:
      curr_count += 1
      max_count = max(max_count, curr_count)
    else:
      curr_count = 1

    prev = curr
    curr = curr.next

  return max_count


def longest_streak(head):
  max_count = 0
  curr_count = 0
  return _longest_streak(head, None, max_count, curr_count)


def _longest_streak(head, prev, max_count, curr_count):
  if head is None:
    return max_count

  if prev is None or head.val == prev.val:
    curr_count += 1
    max_count = max(max_count, curr_count)
  else:
    curr_count = 1

  return _longest_streak(head.next, head, max_count, curr_count)
