"""
dp - ps technique where we:
1. break down our problems into subproblems
2. solve our subproblems
3. utilize our solutions to our subproblems for others

base case-
1. using index pointers to same time (not slicing the array each recursive call)
2. if i or j is at the end of the string, return 0 because empty strings do not have overlaping subsequences

recursive case-

"""

def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, {})

def _overlap_subsequence(s1, s2, i, j, memo):
  key = (i, j)
  if key in memo:
    return memo[key]

  if i == len(s1) or j == len(s2):
    return 0

  max_subsequence = 0
  if s1[i] == s2[j]:
    max_subsequence += 1 + _overlap_subsequence(s1, s2, i + 1, j + 1, memo)
  else:
    first = _overlap_subsequence(s1, s2, i + 1, j, memo)
    second = _overlap_subsequence(s1, s2, i, j + 1, memo)
    max_subsequence += max(first, second)

  memo[key] = max_subsequence
  return max_subsequence

