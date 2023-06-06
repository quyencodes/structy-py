"""
dp - ps technique where we:
1. break down our problems into subproblems
2. solve our subproblems
3. reuse our solutions to solve other subproblems

base case:
s is empty: return True

recursive case:
1. iterate through words
2. if theres a match

"""

def can_concat(s, words):
  return _can_concat(s, 0, words, {})

def _can_concat(s, i, words, memo):
  if i in memo:
    return memo[i]

  if i >= len(s):
    return True

  for word in words:
    pos = len(word)
    match = s[i:i+pos]
    if match == word:
      if _can_concat(s, i + pos, words, memo):
        memo[i] = True
        return True

  memo[i] = False
  return False
