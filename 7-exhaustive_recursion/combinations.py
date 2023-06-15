def create_combinations(items, k):
  # two base cases
  if k == 0:
    return [ [] ]

  if len(items) < k:
    return []

  # two recursive calls
  first = items[0]
  combinations = create_combinations(items[1:], k-1)

  # recursive code
  main_combinations = []
  for combo in combinations:
    temp = [first, *combo]
    main_combinations.append(temp)

  sub_combinations = create_combinations(items[1:], k)

  return main_combinations + sub_combinations

# two base cases
# if k == 0: return [ [] ]
# if items.length < k: return []

# recursive case - lower k and lower items

# recursive case - keep k, lower items
