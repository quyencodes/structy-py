def string_search(grid, s):
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if dfs(grid, r, c, s):
        return True
  return False

def dfs(grid, r, c, s):
  if s == '':
    return True

  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])

  if not row_inbounds or not col_inbounds:
    return False

  if grid[r][c] != s[0]:
    return False

  char = grid[r][c]
  grid[r][c] = '*'
  result = dfs(grid, r-1, c, s[1:]) or dfs(grid, r+1, c, s[1:]) or dfs(grid, r, c-1, s[1:]) or dfs(grid, r, c+1, s[1:])
  grid[r][c] = char
  return result