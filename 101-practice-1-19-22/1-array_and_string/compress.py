def compress(s):
  s += '!'
  i = 0
  j = 0
  result = []
  while i < len(s):
    if s[i] != s[j]:
      if len(s[j:i]) == 1:
        result.append(s[j])
      else:
        group = str(len(s[j:i])) + s[j]
        result.append(group)
      j = i

    i += 1

  return ''.join(result)

#      i
# ccaaatsss!
#   j