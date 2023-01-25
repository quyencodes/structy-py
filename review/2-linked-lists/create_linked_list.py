# input - values
# output - new linked list
# constraints - none
# edge cases - none

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# recursively
def create_linked_list(values, index=0):
  if index == len(values):
    return None

  new_node = Node(values[index])
  new_node.next = create_linked_list(values, index + 1)
  return new_node

def create_linked_list(values):
  if len(values) == 0:
    return None

  new_node = Node(values[0])
  new_node.next = create_linked_list(values[1:])
  return new_node

# iteratively
def create_linked_list(values):
  dummy_head = Node(None)
  current = dummy_head
  for val in values:
    current.next = Node(val)
    current = current.next

  return dummy_head.next