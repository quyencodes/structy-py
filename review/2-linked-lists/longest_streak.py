# iterative
# time - o(n)
# space - o(1)
def longest_streak(head):
  prev = None
  current = head
  longest_streak = 0
  current_streak = 0
  while current:
    if prev is None or prev.val == current.val:
      current_streak += 1
    else:
      current_streak = 1

    if longest_streak < current_streak:
      longest_streak = current_streak

    prev = current
    current = current.next

  return longest_streak

def longest_streak(head, current_streak = 1, longest = 0):
  if head is None:
    return longest

  if head.next is None:
    final_check = max(current_streak, longest)
    return final_check

  if head.val == head.next.val:
    new_current = current_streak + 1
    new_longest = max(longest, new_current)
    return longest_streak(head.next, new_current, new_longest)
  else:
    return longest_streak(head.next, 1, longest)