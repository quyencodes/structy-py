"""
dp - ps technique where we:
1. break down our problems into subproblems
2. solve our subproblems
3. reuse our solutions for other subproblems (memoization)

nodes - subproblems
edges - decisions we make

base case:
one length palindrome: 1
0 length palindrome: 0

recursive case:
1. if first and last char match ->
look at first and last character to see if a match, remove both characters (2 along the edge)
2. if they do NOT match ->
remove first char and last char and call recursively (0 along the edge)
- two recursive calls
"""

def max_palin_subsequence(string):
  start = 0
  end = len(string) - 1
  return _max_palin_subsequence(string, start, end, {})

def _max_palin_subsequence(string, start, end, memo):
  key = (start, end)
  if key in memo:
    return memo[key]

  if start > end:
    return 0

  if start == end:
    return 1

  first_char = string[start]
  last_char = string[end]
  max_len = 0

  if first_char == last_char:
    max_len += 2 + _max_palin_subsequence(string, start + 1, end - 1, memo)
  else:
    remove_first_char = _max_palin_subsequence(string, start + 1, end, memo)
    remove_last_char = _max_palin_subsequence(string, start, end - 1, memo)
    max_len += max(remove_first_char, remove_last_char)

  memo[key] = max_len
  return max_len


