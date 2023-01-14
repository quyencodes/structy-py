# input - grid 2x2 array
# output - number of islands in the grid
# constraints - none
# edge cases - none

# depth first search

def island_count(grid):
  visited = set()
  count = 0
  # iterate through the islands by column
  for r in range(len(grid)):
    # iterate through the islands by row
    for c in range(len(grid[0])):
      # recursively call by row and column
      if explore_island(grid, r, c, visited) == True:
        count += 1
  return count

def explore_island(grid, r, c, visited):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])

  if not row_inbounds or not col_inbounds:
    return False

  if grid[r][c] == "W":
    return False

  pos = (r, c)
  if pos in visited:
    return False

  visited.add(pos)

  # up
  explore_island(grid, r - 1, c, visited)
  # down
  explore_island(grid, r + 1, c, visited)
  # left
  explore_island(grid, r, c - 1, visited)
  # right
  explore_island(grid, r, c + 1, visited)

  return True

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'L', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'W', 'W'],
]
