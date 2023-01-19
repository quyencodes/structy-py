def uncompress(s):
  i = 0
  j = 0
  nums = '0123456789'
  result = ''
  while i < len(s):
    if s[i] not in nums:
      chars = s[i] * int(s[j:i])
      result += chars
      j = i + 1

    i += 1
  return result

#.           j
example = '2c3a1t'
#.            i
# result =