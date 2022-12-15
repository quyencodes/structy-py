from collection import Counter

def most_frequent_char(s):
  count = {}
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1

  highest_freq = None
  for letter in s:
    if highest_freq is None or count[letter] > count[highest_freq]:
      highest_freq = letter

  return highest_freq






# from math import inf

# def most_frequent_char(s):
#   hash_map = {}

#   for char in s:
#     if char not in hash_map:
#       hash_map[char] = 0
#     hash_map[char] += 1

#   highest_freq = -inf
#   char = None
#   for key, value in hash_map.items():
#     if highest_freq < value:
#       highest_freq = value
#       char = key

#   return char

# test1 = most_frequent_char('david')

# print(test1)