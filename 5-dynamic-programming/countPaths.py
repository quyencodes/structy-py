"""
dp - a problem solving technique where:
1) we break down our problem into subproblems
2) solve our subproblems
3) reuse our solutions to our subproblems to other subproblems

nodes - current subproblem
edges - decisions we make

base cases:
1) if we go out of bounds
2) if we hit the bottom-right corner

recursive cases:
1) recurse to right and down

"""


def count_paths(grid):
  memo = {}
  return _count_paths(grid, 0, 0, memo)


def _count_paths(grid, r, c, memo):
  pos = (r, c)
  row_inbounds, col_inbounds = 0 <= r < len(grid), 0 <= c < len(grid[0])
  if pos in memo:
    return memo[pos]

  if not row_inbounds or not col_inbounds or grid[r][c] == 'X':
    return 0

  if r == len(grid) - 1 and c == len(grid[-1]) - 1:
    return 1

  memo[pos] = _count_paths(grid, r + 1, c, memo) + \
      _count_paths(grid, r, c + 1, memo)
  return memo[pos]
