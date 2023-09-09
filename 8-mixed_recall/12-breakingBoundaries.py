def breaking_boundaries(m, n, k, r, c):
  memo = {}
  return _breaking_boundaries(m, n, k, r, c, memo)


def _breaking_boundaries(m, n, k, r, c, memo):
  row_inbounds = 0 <= r < m
  col_inbounds = 0 <= c < n
  key = (k, r, c)

  if key in memo:
    return memo[key]

  if not row_inbounds or not col_inbounds:
    return 1

  if k == 0:
    return 0

  deltas = [(1, 0), (-1, 0), (0, -1), (0, 1)]
  total_count = 0
  for delta in deltas:
    d_row, d_col = delta
    total_count += _breaking_boundaries(m, n, k-1, r + d_row, c + d_col, memo)
  memo[key] = total_count
  return total_count


"""
[
  [x, x, x, x],
  [x, x, x, x],
  [x, x, x, x]
]

(0, 0), k = 2


"""