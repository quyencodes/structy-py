def add_lists(head_1, head_2, carry = 0):
  if head_1 is None and head_2 is None and carry == 0:
    return None

  val_1 = 0 if head_1 is None else head_1.val
  val_2 = 0 if head_2 is None else head_2.val

  sum = val_1 + val_2 + carry
  next_carry = 1 if sum > 9 else 0
  col_sum = sum % 10

  new_node = Node(col_sum)
  new_node.next = add_lists(head_1.next, head_2.next, next_carry)

  return new_node