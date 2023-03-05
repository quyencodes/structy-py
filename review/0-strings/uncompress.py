# n, m - groups of n (letters) and m (numbers)
# time - o(n*m)
# space - o(n*m)
def uncompress(s):
  i = 0
  j = 0
  res = []
  nums = '0123456789'
  while j < len(s):
    if s[j] in nums:
      j += 1
    else:
      letters = int(s[i:j]) * s[j]
      res.append(letters)
      i = j + 1
      j = i

  return ''.join(res)
"""
res = ''.join([])
  i
2c3a1t
  j

i = starting point of nums
j = find a char


"""