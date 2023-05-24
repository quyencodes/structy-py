"""
dp - ps technique where we:
1. break our problem down into subproblems
2. solve our subproblems -> subsolutions
3. reuse solutions to subproblems

base cases:
- out of bounds
- bottom right

recursive cases:
- go right
- go down

brute force
time - o(2**(r+c))
space - o(r+c)

optimal
time - o(r*c)
space - o(r*c)

"""


def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, r, c, memo):
  pos = (r, c)

  if pos in memo:
    return memo[pos]

  if r == len(grid) or c == len(grid[0]):
    return float("-inf")

  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return grid[r][c]

  down_path = _max_path_sum(grid, r+1, c, memo)
  right_path = _max_path_sum(grid, r, c+1, memo)

  memo[pos] = grid[r][c] + max(down_path, right_path)
  return grid[r][c] + max(down_path, right_path)

