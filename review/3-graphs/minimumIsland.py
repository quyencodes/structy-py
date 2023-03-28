"""
time - o(r*c)
space - o(r*c)
"""

def minimum_island(grid):
  count, visited = float("inf"), set()
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      curr = explore_island(grid, r, c, visited)
      if curr != 0 and curr < count:
        count = curr
  return count

def explore_island(grid, r, c, visited):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])

  if not row_inbounds or not col_inbounds:
    return 0

  if grid[r][c] == 'W':
    return 0

  if (r, c) in visited:
    return 0

  visited.add((r, c))

  current = 1
  deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  for d_row, d_col in deltas:
    n_row, n_col = d_row + r, d_col + c
    current += explore_island(grid, n_row, n_col, visited)

  return current