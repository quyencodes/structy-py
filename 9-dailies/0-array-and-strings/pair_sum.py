def pair_sum(numbers, target_sum):
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      if numbers[i] + numbers[j] == target_sum:
        return (i, j)

def pair_sum(numbers, target_sum):
  hash_map = {}
  for index, num in enumerate(numbers):
    difference = target_sum - num
    if difference in hash_map:
      return (hash_map[difference], index)
    else:
      hash_map[num] = index


# {
#   3: 0,
#   2: 1,
#   5: 2,
#   4: 3,
#   1: 4
# }