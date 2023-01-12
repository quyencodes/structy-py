def zipper_lists(head_1, head_2):
  tail = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      tail.next = current_2
      current_2 = current_2.next
    if count % 2 == 1:
      tail.next = current_1
      current_1 = current_1.next
    tail = tail.next
    count += 1

  if current_1 is None:
    tail.next = current_2
  if current_2 is None:
    tail.next = current_1

  return head_1

#  a -> b -> c -> None
#      curr
#  x -> y -> z -> None
#      curr

# count = 2
# a -> x -> b -> y

def zipper_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None

  if head_1 is None:
    return head_2

  if head_2 is None:
    return head_1

  saved_h1 = head_1.next
  saved_h2 = head_2.next
  head_1.next = head_2
  head_2.next = zipper_lists(saved_h1, saved_h2)
  return head_1

# a -> b -> c -> d -> e -> f

# x -> y -> z

# output = a -> x -> b -> y -> c -> z -> d -> e -> f -> None

# zipper_lists(a, x)
# saved_h1 = b
# saved_h2 = y
# a.next = x
# x.next = zipper_lists(b, y)

# x.next = zipper_lists(b, y)
# saved_h1 = c
# saved_h2 = z
# b.next = y
# y.next = zipper_lists(c, z)
# return b -> y -> c -> z -> d

# y.next = zipper_lists(c, z)
# saved_h1 = d
# saved_h2 = None
# c.next = z
# z.next = zipper_lists(d, None) == d
# return c -> z -> d

# z.next = zipper_lists(d, None)
# if head_2 is None:
# return h1 == d
#
#
#
#
#
