def longest_streak(head):
  current_streak, max_streak = 0, 0
  prev = None
  current = head

  while current is not None:
    if prev is None or prev.val == current.val:
      current_streak += 1
      max_streak = max(max_streak, current_streak)
    else:
      current_streak = 1

    prev = current
    current = current.next

  return max_streak