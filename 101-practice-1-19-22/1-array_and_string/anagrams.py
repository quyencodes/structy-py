from collections import Counter
def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)

from collections import Counter
def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)

def char_count(string):
  map = {}
  for char in string:
    if char not in map:
      map[char] = 0
    map[char] += 1

  return map