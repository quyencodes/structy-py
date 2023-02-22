class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

import math
def middle_value(head):
  values = []
  explore_nodes(head, values)

  midpoint = len(values) / 2 if len(values) % 2 == 0 else math.floor(len(values) / 2)

  print(find_middle_value(head, midpoint))
  # return values[midpoint]
  return find_middle_value(head, midpoint)


def explore_nodes(head, values):
  current = head

  while current:
    values.append(current.val)
    current = current.next

  return values

def find_middle_value(head, midpoint):
  if midpoint == 0:
    return head.val

  return find_middle_value(head.next, midpoint - 1)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f
middle_value(a) # d

def middle_value(head):
  slow = head
  fast = head
  while not (fast is None or fast.next is None):
    slow = slow.next
    fast = fast.next.next
  return slow.val