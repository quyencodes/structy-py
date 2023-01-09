from collections import Counter

def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)

def char_count(s):
  hash_map = {}
  for letter in s:
    if letter not in hash_map:
      hash_map[letter] = 0

    hash_map[letter] += 1
  return hash_map

def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)