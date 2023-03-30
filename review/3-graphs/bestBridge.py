from collections import deque
def best_bridge(grid):
  main_island = None

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 'L' and main_island == None:
        main_island = dfs(grid, r, c, set())

  visited = set(main_island)
  queue = deque([(r, c, 0) for r, c in main_island])
  deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  while queue:
    r, c, distance = queue.popleft()

    if grid[r][c] == 'L' and (r, c) not in main_island:
      return distance - 1

    for delta in deltas:
      d_row, d_col = delta
      n_row, n_col = d_row + r, d_col + c
      if is_inbounds(grid, n_row, n_col) and (n_row, n_col) not in visited:
        queue.append((n_row, n_col, distance + 1))
        visited.add((n_row, n_col))

  return -1

def dfs(grid, r, c, visited):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])

  if not is_inbounds(grid, r, c):
    return

  if grid[r][c] == 'W':
    return

  if (r, c) in visited:
    return

  visited.add((r, c))

  dfs(grid, r-1, c, visited)
  dfs(grid, r+1, c, visited)
  dfs(grid, r, c-1, visited)
  dfs(grid, r, c+1, visited)

  return visited

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
print(best_bridge(grid))
