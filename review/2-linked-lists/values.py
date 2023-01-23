# so let me just repeat the question back to you to make sure I understand. From what I understand

# input - head of a linked list
# output - a list with all the linked list values
# constraints - none
# edge cases - none
def linked_list_values(head):
  values = []
  # traversal logic
  get_values(head, values)
  return values

def get_values(head, values):
  # base cases
  if head is None:
    return

  values.append(head.val)

  get_values(head.next, values)

# iterative
def linked_list_values(head):
  values = []
  current = head
  while current:
    values.append(current.val)
    current = current.next
  return values
