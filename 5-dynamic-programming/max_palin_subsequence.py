def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string)-1, {})

def _max_palin_subsequence(string, i, j, memo):
  if (i, j) in memo:
    return memo[(i, j)]

  if i == j:
    memo[(i, j)] = 1
    return 1

  if i > j:
    memo[(i, j)] = 0
    return 0

  if string[i] == string[j]:
    memo[(i, j)] = 2 + _max_palin_subsequence(string, i+1, j-1)
  else:
    memo[(i, j)] = max(_max_palin_subsequence(string, i + 1, j), _max_palin_subsequence(string, i, j - 1))

  return memo[(i, j)]