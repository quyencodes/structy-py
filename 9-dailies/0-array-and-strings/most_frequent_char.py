# more optimal solution
from collections import Counter

def most_frequent_char(s):
  count_map = Counter(s)
  max = float("-inf")
  result = ''
  for letter, count in count_map.items():
    if count > max:
      max = count
      result = letter

  return result


def most_frequent_char(s):
  count = count_char(s)
  max = float('-inf')
  result = ''
  for letter, count in count.items():
    if count > max:
      max = count
      result = letter
  return result

def count_char(s):
  hash_map = {}
  for letter in s:
    if letter not in hash_map:
      hash_map[letter] = 0

    hash_map[letter] += 1

  return hash_map

# solution from structy
def most_frequent_char(s):
  count = count_char(s)
  best = None
  for letter in count:
    if best is None or count[letter] > count[best]:
      best = letter
  return best