def string_search(grid, s):
  visited = set()
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if _string_search(grid, r, c, s, visited, 0):
        return True

  return False

def _string_search(grid, r, c, s, visited, i):
  if i == len(s):
    return True

  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  key = (r, c)

#   if key in visited:
#     return False
#   visited.add(key)

  if not row_inbounds or not col_inbounds:
    return False

  if grid[r][c] != s[i]:
    return False

  deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  char = grid[r][c]
  for delta in deltas:
    delta_row, delta_col = delta
    new_row, new_col = r + delta_row, c + delta_col
    grid[r][c] = '*'
    if _string_search(grid, new_row, new_col, s, visited, i+1):
      return True

  grid[r][c] = char
  return False




