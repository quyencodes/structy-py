def subsets(elements):
  return _subsets(elements, 0)

def _subsets(elements, i):
  if len(elements) == 0:
    return [ [] ]

  first = elements[0] # 'a'
  subsets_without = _subsets(elements[1:], i+1) # [ ['b', 'c'], ['c'], ['b'], [] ]

  subsets_with = []
  for subset in subsets_without:
    subsets_with.append([first, *subset])

  return subsets_with + subsets_without



