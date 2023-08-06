class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def insert_node(head, value, index):
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head

  prev = None
  curr = head
  while curr:
    if index == 0:
      val = Node(value)
      prev.next = val
      val.next = curr
      return head

    prev = curr
    curr = curr.next
    index -= 1

  if index == 0:
    prev.next = Node(value)

  return head
