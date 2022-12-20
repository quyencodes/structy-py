class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

def longest_streak(head):
  current = head
  max_streak = 0
  curr_streak = 0
  prev = None

  while current is not None:
    if prev != current.val:
      curr_streak = 1
    else:
      curr_streak += 1

    if max_streak < curr_streak:
      max_streak = curr_streak

    prev = current.val
    current = current.next

  return max_streak

# recursive solution
def longest_streak(head):

