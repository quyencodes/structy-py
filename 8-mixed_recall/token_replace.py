def token_replace(s, tokens):
  i = 0
  j = 1
  res = []
  while i < len(s):
    if s[i] != '$':
      res.append(s[i])
      i += 1
      j += 1
    elif s[j] != '$':
      j += 1
    else:
      key = s[i:j + 1]
      res.append(tokens[key])
      i = j + 1
      j = i + 1

  return ''.join(res)