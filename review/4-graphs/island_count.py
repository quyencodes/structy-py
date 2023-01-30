# input - n*n grid with ws representing water and ls representing land
# island is a connected body of ls
# output - number of islands

def island_count(grid):
  visited = set()
  num_islands = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if explore_island(grid, r, c, visited) == True:
        num_islands += 1
  return num_islands

def explore_island(grid, r, c, visited):
  if not is_inbounds(grid, r, c):
    return False

  if grid[r][c] == 'W':
    return False

  pos = (r, c)
  if pos in visited:
    return False

  visited.add(pos)

  deltas = [
    (-1, 0), # row up
    (1, 0), # row down
    (0, 1), # column right
    (0, -1) # column left
  ]

  for delta in deltas:
    delta_row, delta_col = delta
    neighbor_row = delta_row + r
    neighbor_col = delta_col + c
    explore_island(grid, neighbor_row, neighbor_col, visited)

  return True

def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds

explore_island(grid, r - 1, c, visited) # up
explore_island(grid, r + 1, c, visited) # down
explore_island(grid, r, c + 1, visited) # right
explore_island(grid, r, c - 1, visited) # left


def island_count(grid):
  visited = set()
  num_islands = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if explore_island(grid, r, c, visited) == True:
        num_islands += 1
  return num_islands

def explore_island(grid, r, c, visited):
  if not is_inbounds(grid, r, c):
    return False

  if grid[r][c] == 'W':
    return False

  pos = (r, c)
  if pos in visited:
    return False

  visited.add(pos)

  explore_island(grid, r+1, c, visited) # down
  explore_island(grid, r-1, c, visited) # up
  explore_island(grid, r, c+1, visited) # right
  explore_island(grid, r, c-1, visited) # left

  return True

def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds