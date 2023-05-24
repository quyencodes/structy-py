"""
dp - problem solving technique where we break down our problems into subproblems, solve the
subproblems, use the solutions to the subproblems to other subproblems

nodes - subproblems
edges - decisions we take

base cases:
if out_of_bounds: return
if r == len(grid) - 1 and c == len(grid[0]) - 1: return 1

recursive cases:
1. go down
2. go right

brute force:
time - o(2**(r+c))
space - o(r+c)

optimal:
time - o(r*c)
space - o(r*c)

"""

def count_paths(grid):
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r, c, memo):
  pos = (r, c)
  if pos in memo:
    return memo[pos]

  if not is_inbounds(grid, r, c):
    return 0

  if grid[r][c] == 'X':
    return 0

  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return 1

  countP = 0
  countP += _count_paths(grid, r+1, c, memo)
  countP += _count_paths(grid, r, c+1, memo)

  memo[pos] = countP
  return memo[pos]

def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds
