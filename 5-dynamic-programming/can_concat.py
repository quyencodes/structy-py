def can_concat(s, words):
  return _can_concat(s, words, {})
def _can_concat(s, words, memo):
  if s in memo:
    return memo[s]

  if s == '':
    return True

  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      if can_concat(suffix, words) == True:
        memo[s] = True
        return True

  memo[s] = False
  return False

def can_concat(s, words):
  return _can_concat(s, words, '', {})

def _can_concat(s, words, temp, memo):
  if temp in memo:
    return memo[temp]

  if len(temp) > len(s):
    memo[temp] = False
    return False

  if temp == s:
    memo[temp] = True
    return True

  for word in words:
    res = ''
    res += temp
    res += word
    if _can_concat(s, words, res, memo) == True:
      return True

  memo[temp] = False
  return memo[temp]

can_concat("oneisnone", ["one", "is", "none"]) #  -> True