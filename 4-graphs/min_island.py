def minimum_island(grid):
  visited = set()
  minimum_island = float("+inf")

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      size = explore(grid, r, c, visited)
      if size > 0 and minimum_island > size:
        minimum_island = size
  return minimum_island

def explore(grid, r, c, visited):
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

  return 1 + explore(grid, r - 1, c, visited) + explore(grid, r + 1, c, visited) + explore(grid, r, c - 1, visited) + explore(grid, r, c + 1, visited) # right


