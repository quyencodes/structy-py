def permutations(items):
  return _permutations(items, 0)

def _permutations(items, i):
  if len(items) == i:
    return [ [] ]

  first = items[i] # 'a'
  perms_without_first = _permutations(items, i+1) # [['b', 'c'], ['c', 'b']]

  full_permutations = []
  for perm in perms_without_first:
    for k in range(len(perm) + 1):
      temp = perm[:k] + [first] + perm[k:]
      full_permutations.append(temp)

  return full_permutations