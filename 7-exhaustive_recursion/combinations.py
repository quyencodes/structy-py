def create_combinations(items, k):
  if k == 0:
    return [[]]

  if k > len(items):
    return []

  first = items[0]
  partial_combos = create_combinations(items[1:], k-1) # [b], [c]

  combos_with_first = []
  for partial_combo in partial_combos:
    combos_with_first.append([ first, * partial_combo ])

  combos_without_first = create_combinations(items[1:], k) # [[b, c]]
  return combos_with_first + combos_without_first

create_combinations(["a", "b", "c"], 2); # ->
