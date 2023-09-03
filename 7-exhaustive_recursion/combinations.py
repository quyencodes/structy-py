"""
['a', 'b'], 2

base cases:
1. if k == 0: return [[]]
2. if k > len(items): return []

recursive case:
1. make both inputs smaller
2. make only items smaller

"""


def create_combinations(items, k):
  if k == 0:
    return [[]]

  if k > len(items):
    return []

  ele = items[0]
  combinations = create_combinations(items[1:], k - 1)  # [[]]
  with_first = []
  for comb in combinations:
    with_first.append([ele] + comb)

  without_first = create_combinations(items[1:], k)  # [['b']]
  return with_first + without_first


example1 = [['a', 'b']]
example2 = ['c', 'd']
print(example1 + example2)
