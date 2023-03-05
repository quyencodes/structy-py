def pair_sum(numbers, target_sum):
  prev_numbers = {}

  for index, num in enumerate(numbers):
    complement = target_sum - num

    if complement in prev_numbers:
      return (index, prev_numbers[complement])

    prev_numbers[num] = index