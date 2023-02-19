def subsets(elements):
  if len(elements) == 0:
    return [[]]

  first = elements[0] # a
  subs_without_first = subsets(elements[1:]) # [b, c]

  subs_with_first = []
  for sub in subs_without_first:
    subs_with_first.append([first, *sub])

  return subs_without_first + subs_with_first

print(subsets(['a', 'b'])) # ->
# [
#   [],
#   [ 'b' ],
#   [ 'a' ],
#   [ 'a', 'b' ]
# ]


def subsets(elements):
  res = _subsets(elements, 0, [])
  return res

def _subsets(elements, i, values):
  if i >= len(elements):
    return values

  new_values = [*values, elements[i]]
  # print('values:', values)
  # print('new values:', new_values)
  exclude = _subsets(elements, i+1, values) # []
  include = _subsets(elements, i+1, new_values) # []

  return [exclude, include]

print(subsets(['a', 'b'])) # ->
# [
#   [],
#   [ 'b' ],
#   [ 'a' ],
#   [ 'a', 'b' ]
# ]

# exclude(elements, 0, [])
# exclude(elements, 1, [])
# exclude(elements, 2, [])
# - exclude(elements, 3, []) -> returns []
# - include(elements, 3, [c]) -> returns [c]