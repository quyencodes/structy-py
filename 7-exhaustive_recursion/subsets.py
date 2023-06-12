def subsets(elements):
  return _subsets(elements, 0)

def _subsets(elements, i):
  if len(elements) == i:
    return [ [] ]

  first = elements[i] # 'a'
  subsets_without = _subsets(elements, i+1) # [ ['b', 'c'], ['c'], ['b'], [] ]

  subsets_with = []
  for subset in subsets_without:
    subsets_with.append([first, *subset])

  return subsets_with + subsets_without



