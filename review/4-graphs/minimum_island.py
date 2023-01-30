# input - n x n grid
# output - size of the smallest island within the grid
def minimum_island(grid):
  visited = set()
  smallest_island = float('+inf')
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      count = explore_island(grid, r, c, visited)
      if count < smallest_island and count != 0:
        smallest_island = count
  return smallest_island

def explore_island(grid, r, c, visited):
  if not is_inbounds(grid, r, c):
    return 0

  if grid[r][c] == 'W':
    return 0

  pos = (r, c)
  if pos in visited:
    return 0
  visited.add(pos)

  return 1 + explore_island(grid, r+1, c, visited) + explore_island(grid, r-1, c, visited) + explore_island(grid, r, c+1, visited) + explore_island(grid, r, c-1, visited)

def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds