def most_frequent_char(s):
  map = {}
  best = None

  for char in s:
    if char not in map:
      map[char] = 0
    map[char] += 1

  for ele in map:
    if best is None or map[ele] > map[best]:
      best = ele

  return best

from collections import Counter
def most_frequent_char(s):
  map = Counter(s)
  best = None
  for key, value in map.items():
    if best is None or value > map[best]:
      best = key

  return best