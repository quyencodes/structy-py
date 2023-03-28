"""
time - o(r*c)
space - o(r*c)
"""

from collections import deque
def closest_carrot(grid, starting_row, starting_col):
  queue = deque([(starting_row, starting_col, 0)])
  visited = set()
  visited.add((starting_row, starting_col, 0))
  deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  while queue:
    r, c, distance = queue.popleft()

    if grid[r][c] == 'C':
      return distance

    for delta in deltas:
      d_row, d_col = delta
      n_row, n_col = d_row + r, d_col + c
      if is_inbounds(grid, n_row, n_col) and grid[n_row][n_col] != 'X' and (n_row, n_col) not in visited:
        queue.append((n_row, n_col, distance+1))
        visited.add((n_row, n_col))

  return -1

def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds