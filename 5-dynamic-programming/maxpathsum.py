def max_path_sum(grid):
  memo = {}
  res = _max_path_sum(grid, 0, 0, memo)
  return res

def _max_path_sum(grid, r, c, memo):
  if (r, c) in memo:
    return memo[(r, c)]

  if not is_inbounds(grid, r, c):
    return 0

  if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
    return grid[r][c]

  down_val = _max_path_sum(grid, r + 1, c, memo) # return an int
  right_val = _max_path_sum(grid, r, c + 1, memo)

  memo[(r, c)] = grid[r][c] + max(down_val, right_val)
  return memo[(r, c)]

def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds