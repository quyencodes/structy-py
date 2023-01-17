from collections import deque
def closest_carrot(grid, starting_row, starting_col):
  visited = set()
  # visited = set([(starting_row, starting_col)])
  queue = deque([ (starting_row, starting_col, 0) ])
  while queue:
    current = queue.popleft()
    row, col, distance = current

    if grid[row][col] == 'C':
      return distance

    pos = (row, col)
    visited.add(pos)
    # row, column changes
    # down, up, right, left
    deltas = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col

      row_inbounds = 0 <= neighbor_row < len(grid)
      col_inbounds = 0 <= neighbor_col < len(grid[0])

      if row_inbounds and col_inbounds and grid[neighbor_row][neighbor_col] != 'X' and (neighbor_row, neighbor_col) not in visited:
        queue.append((neighbor_row, neighbor_col, distance + 1))

  return -1