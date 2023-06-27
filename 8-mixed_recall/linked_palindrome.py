class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def linked_palindrome(head):
  curr = head
  values = []

  while curr is not None:
    values.append(curr.val)
    curr = curr.next

  return curr == curr[::-1]

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_palindrome(head):
  rev_head = reverse_linkedlist(head)
  while head is not None and rev_head is not None:
    if head.val != rev_head.val:
      return False
    head = head.next
    rev_head = rev_head.next

  return True

def reverse_linkedlist(head):
  if head is None:
    return None

  if head.next is None:
    return head

  new_head = reverse_linkedlist(head.next)
  head.next = None
  new_head.next = head
  return new_head