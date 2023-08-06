class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def add_lists(head_1, head_2, carry=0):
  if head_1 is None and head_2 is None and carry == 0:
    return None

  val1 = head_1.val if head_1 is not None else 0
  val2 = head_2.val if head_2 is not None else 0

  next_1 = head_1.next if head_1 is not None else None
  next_2 = head_2.next if head_2 is not None else None

  value = val1 + val2 + carry
  new_carry = 1 if value > 9 else 0
  digit = value % 10
  new_head = Node(digit)
  new_head.next = add_lists(next_1, next_2, new_carry)
  return new_head


"""
No carry case and same length:


Not same length case:

Carry case:
"""
