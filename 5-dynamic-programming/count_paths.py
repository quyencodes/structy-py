def count_paths(grid):
  count = 0
  memo = {}
  count += explore_paths(grid, 0, 0, memo)

  return count

def explore_paths(grid, r, c, memo):
  if (r, c) in memo:
    return memo[(r, c)]

  if not is_inbounds(grid, r, c):
    memo[(r, c)] = 0
    return 0

  if grid[r][c] == 'X':
    memo[(r, c)] = 0
    return 0

  if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
    memo[(r, c)] = 1
    return 1

  count = 0
  count += explore_paths(grid, r + 1, c, memo)
  count += explore_paths(grid, r, c + 1, memo)
  memo[(r, c)] = count
  return count

def is_inbounds(grid, r, c):
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  return row_inbounds and col_inbounds



def example(r, c):
  store = {}
  store[(r, c)] = 1
  if (r, c) in store:
    print(store[(r, c)])

example(1, 2)




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
