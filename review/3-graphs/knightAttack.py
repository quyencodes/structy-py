from collections import deque
def knight_attack(n, kr, kc, pr, pc):
  visited = set()
  visited.add((kr, kc))
  queue = deque([ (kr, kc, 0) ])

  while queue:
    r, c, distance = queue.popleft()

    if (r, c) == (pr, pc):
      return distance

    neighbors = valid_positions(n, r, c)

    for neighbor in neighbors:
      n_row, n_col = neighbor
      if (n_row, n_col) not in visited:
        queue.append((n_row, n_col, distance + 1))
        visited.add((n_row, n_col))

  return None

def valid_positions(n, r, c):
  res = []
  deltas = [
    (-1, -2),
    (-1, 2),
    (1, 2),
    (1, -2),
    (-2, 1),
    (2, 1),
    (-2, -1),
    (2, -1),
  ]

  for delta in deltas:
    d_row, d_col = delta
    n_row, n_col = d_row + r, d_col + c
    if is_inbounds(n, n_row, n_col):
      res.append((n_row, n_col))

  return res

def is_inbounds(n, r, c):
  row_inbounds = 0 <= r < n
  col_inbounds = 0 <= c < n
  return row_inbounds and col_inbounds
