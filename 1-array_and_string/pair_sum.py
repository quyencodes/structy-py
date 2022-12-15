def pair_sum(numbers, target_sum):
  hash_map = {}
  for index, value in enumerate(numbers):
    y = target_sum - value
    if y in hash_map:
      return (hash_map[y], index)
    else:
      hash_map[value] = index


# brute force
def pair_sum(numbers, target_sum):
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == target_sum:
        return (i, j)