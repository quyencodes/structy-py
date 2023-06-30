def binary_search(numbers, target):
  l, r = 0, len(numbers) - 1
  while l <= r:
    midpoint = (l + r) // 2
    if target == numbers[midpoint]:
      return midpoint
    elif target < numbers[midpoint]:
      r = midpoint - 1
    else:
      l = midpoint + 1

  return -1