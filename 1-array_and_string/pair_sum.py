def pair_sum(numbers, target_sum):
  hash_map = {}
  for index, value in enumerate(numbers):
    y = target_sum - value
    if y in hash_map:
      return (hash_map[y], index)
    else:
      hash_map[value] = index