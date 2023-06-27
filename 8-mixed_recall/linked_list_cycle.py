def linked_list_cycle(head, unique=set()):
  if head is None: return False
  curr = head

  while curr is not None:
    if curr.val in unique:
      return True
    unique.add(curr.val)
    curr = curr.next

  return False

def linked_list_cycle(head):
  if head is None: return False
  slow = head
  fast = head.next
  while not (fast is None or fast.next is None):
    if slow is fast:
      return True
    slow = slow.next
    fast = fast.next.next
  return False

l1 = ['a', 'b']
l2 = ['a', 'b']

print(l1 == l2)
print(l1 is l2)
