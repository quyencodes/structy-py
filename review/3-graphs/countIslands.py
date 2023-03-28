"""
brute force solution:
1) initialize count, change the grid itself if visited before 'W'
2) iteratively go through each row x col combination
3) recursively visited the land elements -> return to top level count of 1
4) return count
r - num of rows
c - num of cols
time - o(r*c)
space - o(1)

"""

def island_count(grid):
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if explore(grid, r, c):
        count += 1
  return count

def explore(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])

  if not row_inbounds or not col_inbounds:
    return False

  if grid[r][c] == 'W':
    return False

  grid[r][c] = 'W'

  deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for d_row, d_col in deltas:
    n_row, n_col = d_row + r, d_col + c
    explore(grid, n_row, n_col)

  return True
