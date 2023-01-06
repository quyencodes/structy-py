def uncompress(s):
  i = 0
  j = 0
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  numbers = '0123456789'
  result = ''
  while i < len(s):
    if s[i] in alphabet:
      result += s[i] * int(s[j:i])
      j = i + 1
    i += 1

  return result
