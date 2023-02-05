



from collections import deque
def count_paths(grid):
  corner = (len(grid) - 1, len(grid) - 1)
  count = 0
  queue = deque([(0, 0)])
  while queue:
    current = queue.popleft()
    row, col = current

    if current == corner:
      count += 1

    deltas = [(1, 0), (0, 1)]
    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = delta_row + row
      neighbor_col = delta_col + col
      if is_inbounds(neighbor_row, neighbor_col, grid) and grid[neighbor_row][neighbor_col] != "X":
        queue.append((neighbor_row, neighbor_col))

  return count

def is_inbounds(r, c, grid):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds
