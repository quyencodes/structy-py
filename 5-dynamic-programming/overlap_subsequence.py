def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, {})

def _overlap_subsequence(string_1, string_2, i, j, memo):
  if (i, j) in memo:
    return memo[(i, j)]

  if i >= len(string_1) or j >= len(string_2):
    memo[(i, j)] = 0
    return 0

  if string_1[i] == string_2[j]:
    return 1 + _overlap_subsequence(string_1, string_2, i+1, j+1, memo)

  removeFirstCharS1 = _overlap_subsequence(string_1, string_2, i+1, j, memo)
  removeFirstCharS2 = _overlap_subsequence(string_1, string_2, i, j+1, memo)

  memo[(i,j)] = max(removeFirstCharS1, removeFirstCharS2)
  return memo[(i, j)]
