def quickest_concat(s, words):
  return -1 if _quickest_concat(s, words, {}) == float('inf') else _quickest_concat(s, words, {})

def _quickest_concat(s, words, memo):
  if s in memo:
    return memo[s]

  if s == '':
    return 0

  min_words = float('inf')
  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      attempt = 1 + _quickest_concat(suffix, words, memo)
      min_words = min(min_words, attempt)

  memo[s] = min_words
  return memo[s]

print(quickest_concat('caution', ['ca', 'ion', 'caut', 'ut'])) # -> 2
