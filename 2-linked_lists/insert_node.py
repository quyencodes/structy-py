class Node:
  def __init__(self, value):
    self.value = value
    self.next = next

# iterative approach
def insert_node(head, value, index):
  count = 0
  current = head

  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head

  while current is not None:
    if count == index - 1:
      # insertion
      temp = current.next
      current.next = Node(value)
      current.next.next = temp

    count += 1
    current = current.next

  return head

# recursive approach
def insert_node(head, value, index, count = 0):
  if head is None:
    return None

  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head

  if count == index - 1:
    temp = head.next
    head.next = Node(value)
    head.next.next = temp
    return

  insert_node(head.next, value, index, count += 1)
  return head