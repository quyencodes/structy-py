def pair_product(numbers, target_product):
  prev_numbers = {}
  # enumerate(iterable, start index what you want it to start at)
  for i, num in enumerate(numbers, 0):
    complement = target_product / num
    if complement in prev_numbers:
      return (i, prev_numbers[complement])

    prev_numbers[num] = i