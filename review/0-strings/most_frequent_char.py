def most_frequent_char(s):
  countMap = {}
  for char in s:
    countMap[char] = 1 + countMap.get(char, 0)

  res = None
  for char in s:
    if res is None or countMap[res] < countMap[char]:
      res = char

  return res