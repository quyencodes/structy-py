from collections import deque
def best_bridge(grid):
  # find an island
  main_island = None

  for r in range(len(grid)):
    for c in range(len(grid[0])):
      potential_island = traverse_island(grid, r, c, set())
      if len(potential_island) > 0:
        main_island = potential_island
        break

  visited = set(main_island)
  queue = deque([])
  for position in main_island:
    row, col = position
    queue.append((row, col, 0))

  while queue:
    r, c, distance = queue.popleft()

    if grid[r][c] == 'L' and (r, c) not in main_island:
      return distance - 1

    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_r = delta_row + r
      neighbor_c = delta_col + c
      neighbor_pos = (neighbor_r, neighbor_c)
      if is_inbounds(grid, neighbor_r, neighbor_c) and neighbor_pos not in visited:
        visited.add(neighbor_pos)
        queue.append((neighbor_r, neighbor_c, distance + 1))


def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds

def traverse_island(grid, row, col, visited):
  if not is_inbounds(grid, row, col) or grid[row][col] == 'W':
    return visited

  pos = (row, col)
  if pos in visited:
    return visited

  visited.add(pos)

  traverse_island(grid, row - 1, col, visited)
  traverse_island(grid, row + 1, col, visited)
  traverse_island(grid, row, col - 1, visited)
  traverse_island(grid, row, col + 1, visited)

  return visited


