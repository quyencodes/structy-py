"""
Utilize a stack for intervals. Sort the intervals in ascending order. Iterate through the intervals with a forEach loop.
"""


def combine_intervals(intervals):
  stack = []
  sorted_intervals = sorted(intervals, key=lambda x: x[0], reverse=False)

  for interval in sorted_intervals:
    if not stack:
      stack.append(interval)
      continue

    last_a, last_b = stack[-1]
    curr_a, curr_b = interval

    if curr_a <= last_b:
      stack[-1] = (last_a, max(curr_b, last_b))
    else:
      stack.append(interval)

  return stack


"""
(1, 4), (3, 7), (8, 13), (12, 15)
stack = [(1, 4)]
(1, 4)
(3, 7)

"""
