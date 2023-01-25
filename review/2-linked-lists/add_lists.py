def add_lists(head_1, head_2, carry=0):
  if head_1 is None and head_2 is None and carry == 0:
    return None

  num_1 = 0 if head_1 is None else head_1.val
  num_2 = 0 if head_2 is None else head_2.val
  sum = num_1 + num_2 + carry
  next_carry = 1 if sum > 9 else 0

  digit = sum % 10
  new_num = Node(digit)

  next_1 = None if head_1 is None else head_1.next
  next_2 = None if head_2 is None else head_2.next
  new_num.next = add_lists(next_1, next_2, next_carry)
  return new_num

# iterative
def add_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  current_1 = head_1
  current_2 = head_2
  while current_1 is not None or current_2 is not None or carry == 0:

    num_1 = 0 if current_1 is None else current_1.val
    num_2 = 0 if current_2 is None else current_2.val
    pre_sum = num_1 + num_2
    carry = 1 if pre_sum > 9 else 0
    digit = (pre_sum + carry) % 10

    new_node = Node(digit)
    tail.next = new_node

    current_1 = None if current_1 is None else current_1.next
    current_2 = None if current_2 is None else current_2.next
    tail = tail.next

  return dummy_head.next