def minimum_island(grid):
  visited = set()
  min_value = float("inf")
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      size = explore_size(grid, r, c, visited)
      if size > 0 and size < min_value:
        min_value = size
  return min_value

def explore_size(grid, r, c, visited):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])

  if not row_inbounds or not col_inbounds:
    return 0

  if grid[r][c] == 'W':
    return 0

  pos = (r, c)
  if pos in visited:
    return 0

  visited.add(pos)
  size = 1
  size += explore_size(grid, r - 1, c, visited) # up
  size += explore_size(grid, r + 1, c, visited) # down
  size += explore_size(grid, r, c + 1, visited) # left
  size += explore_size(grid, r, c - 1, visited) # right
  return size