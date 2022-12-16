def pair_product(numbers, target_product):
  hash_map = {}
  for index, value in enumerate(numbers):
    complement = target_product / value
    if complement in hash_map:
      return (hash_map[complement], index)

    hash_map[value] = index