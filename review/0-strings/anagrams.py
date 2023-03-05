"""
anagrams - same number of characters but any order

n = chars of s1
m = chars of s2
time - o(n+m)
space - o(n+m)
"""

import collections
def anagrams(s1, s2):
  return counter(s1) == counter(s2)

def counter(s):
  countMap = {}
  for i in range(len(s)):
    if s[i] not in countMap:
      countMap[s[i]] = 0
    countMap[s[i]] += 1

  return countMap

# return collections.Counter(s1) == collections.Counter(s2)

#   if len(s1) != len(s2):
#     return False

#   map_1, map_2 = {}, {}
#   for i in range(0, len(s1), 1):
#     map_1[s1[i]] = 1 + map_1.get(s1[i], 0)
#     map_2[s2[i]] = 1 + map_2.get(s2[i], 0)

#   return map_1 == map_2
