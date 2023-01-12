# more optimal solution
def pair_product(numbers, target_product):
  # enumerate(list, start_index=0)
  hash_map = {}
  for index, num in enumerate(numbers):
    compliment = target_product / num
    if compliment in hash_map:
      return (hash_map[compliment], index)
    hash_map[compliment] = index

def pair_product(numbers, target_product):
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] * numbers[j] == target_product:
        return (i, j)