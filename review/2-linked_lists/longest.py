# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# iterative
def longest_streak(head):
  prev = None
  current = head

  max_streak = 0
  current_streak = 0

  while current is not None:
    # update current_streak
    if prev is not None and prev.val == current.val:
      current_streak += 1
    else:
      current_streak = 1

    # continue to iterate
    prev = current
    current = current.next

    # update max_streak
    if max_streak < current_streak:
      max_streak = current_streak

  return max_streak
