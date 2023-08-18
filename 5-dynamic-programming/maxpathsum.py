"""
dp - ps technique where we:
1) break down our problem into subproblems
2) solve our subproblems
3) reuse our solutions to our subproblems to other subproblems (memoization)
"""


def max_path_sum(grid):
  memo = {}
  return _mps(grid, 0, 0, memo)


def _mps(grid, r, c, memo):
  pos = (r, c)
  row_inbounds, col_inbounds = 0 <= r < len(grid), 0 <= c < len(grid[0])

  if pos in memo:
    return memo[pos]

  if not row_inbounds or not col_inbounds:
    return 0

  down = _mps(grid, r + 1, c, memo)
  right = _mps(grid, r, c + 1, memo)

  max_path = max(down, right)
  memo[pos] = grid[r][c] + max_path
  return memo[pos]
