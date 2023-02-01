def best_bridge(grid):
  visited = set()
  queue = []
  # find first island
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if explore_islands(grid, r, c, visited, queue) == True:
        print('found an island')
        break
    if len(visited) > 0:
      break
  print(visited)

  # breadth first search
  while queue:
    current = queue.pop(0)
    row, col, distance = current

    deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = delta_row + row
      neighbor_col = delta_col + col
      if is_inbounds(grid, neighbor_row, neighbor_col) and (neighbor_row, neighbor_col) not in visited:
        if grid[neighbor_row][neighbor_col] == 'L':
          return distance
        queue.append((neighbor_row, neighbor_col, distance + 1))
        visited.add((neighbor_row, neighbor_col))

def explore_islands(grid, r, c, visited, queue):
  if not is_inbounds(grid, r, c):
    return False

  if grid[r][c] == 'W':
    return False

  pos = (r, c)
  if pos in visited:
    return False
  visited.add(pos)
  queue.append((r, c, 0))

  explore_islands(grid, r-1, c, visited, queue) # up
  explore_islands(grid, r+1, c, visited, queue) # down
  explore_islands(grid, r, c+1, visited, queue) # left
  explore_islands(grid, r, c-1, visited, queue) # right

  return True

def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds

grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
best_bridge(grid) # -> 1