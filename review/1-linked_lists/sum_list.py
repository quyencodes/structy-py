# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# recursively
# time - o(n)
# space - o(n)

# iteratively
# time - o(n)
# space - o(1)

def sum_list(head, num=0):
  if head is None:
    return num

  num += head.val
  return sum_list(head.next, num)