def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)


def char_count(s):
  hash_map = {}
  for char in s:
    if char not in hash_map:
      hash_map[char] = 0
    # increment
    hash_map[char] += 1

  return hash_map

# def anagrams(s1, s2):
#   hash_map1 = {}
#   hash_map2 = {}

#   # if the two words do not have the same length, return false
#   if len(s1) != len(s2):
#     return False

#   for i in range(len(s1)):
#     # if property is undefined, set to 1
#     if s1[i] not in hash_map1:
#       hash_map1[s1[i]] = 1
#     # if property exists, increment by 1
#     elif i in hash_map1:
#       hash_map1[s1[i]] += 1

#     if s2[i] not in hash_map2:
#       hash_map2[s2[i]] = 1
#     elif s2[i] in hash_map2:
#       hash_map2[s2[i]] += 1

#   # check for each letter
#   for k, v in hash_map1.items():
#     if hash_map2.get(k) is None and hash_map2.get(k) != v:
#       return False

#   return True

#   print("hash_map1:", hash_map1)
#   print("hash_map2:", hash_map2)

# # test1 = anagrams('cats', 'tocs')
# # test2 = anagrams('restful', 'fluster')

# print(test1)