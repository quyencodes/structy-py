def uncompress(s):
  i = 0
  j = 0
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  result = ''
  while i < len(s):
    if s[i] in alphabet:
      result += s[i] * int(s[j:i])
      j = i + 1
    i += 1

  return result

def uncompress(s):
  i = 0
  j = 0
  numbers = '0123456789'
  result = []

  while j < len(s):
    if s[j] in numbers:
      j += 1

    else:
      num = int(s[i:j])
      result.append(num * s[j])
      j += 1
      i = j

  return ''.join(result)