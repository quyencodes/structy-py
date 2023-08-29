"""
Take/Don't Take Algorithm. Base case: return a 2d matrix when i == len(elements). Use an index variable for better time complexity. Isolate elements[i]. Recursive call for i+1. Add first to the without_first list and return them together.
"""


def subsets(elements):
  return _subsets(elements, 0)


def _subsets(elements, i):
  if i == len(elements):
    return [[]]

  first = elements[i]
  without_first = _subsets(elements, i + 1)  # [[], ['b'], ['c'], ['b', 'c']]

  with_first = []
  for sublist in without_first:
    temp = [first] + sublist
    with_first.append(temp)

  return with_first + without_first
