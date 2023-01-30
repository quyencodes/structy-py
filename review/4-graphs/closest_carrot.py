from collections import deque
def closest_carrot(grid, starting_row, starting_col):
  visited = set([(starting_row, starting_col)])
  queue = deque([(starting_row, starting_col, 0)])
  while queue:
    current = queue.popleft()
    row, col, distance = current

    if grid[row][col] == 'C':
      return distance

    # up, down, left, right
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = delta_row + row
      neighbor_col = delta_col + col
      if is_inbounds(grid, neighbor_row, neighbor_col) and (neighbor_row, neighbor_col) not in visited and grid[neighbor_row][neighbor_col] != 'X':
        queue.append((neighbor_row, neighbor_col, distance + 1))
        visited.add((neighbor_row, neighbor_col))

  return -1

def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds

grid = [
  ['O', 'O', 'X', 'C', 'O'],
  ['O', 'X', 'X', 'X', 'O'],
  ['C', 'X', 'O', 'O', 'O'],
];

print(closest_carrot(grid, 2, 2)) # -> 5