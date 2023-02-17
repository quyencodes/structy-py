def knightly_number(n, m, kr, kc, pr, pc):
  return _knightly_number(n, m, kr, kc, pr, pc, {})


def _knightly_number(n, m, kr, kc, pr, pc, memo):
  if (m, kr, kc) in memo:
    return memo[(m, kr, kc)]

  if m < 0:
    return 0

  if (kr, kc) == (pr, pc) and m == 0:
    return 1 # amount of times knight can move to the target

  moves = [
    (-2, -1), # upleft
    (-2, 1), # upright
    (-1, -2), # midupleft
    (-1, 2), # midupright
    (1, -2), # midbottomleft
    (1, 2), # midbottomright
    (2, -1), # bottomleft
    (2, 1), # bottomright
  ]

  knightly_num = 0
  for move in moves:
    delta_row, delta_col = move
    new_kr = kr + delta_row
    new_kc = kc + delta_col
    if is_inbounds(n, new_kr, new_kc):
      knightly_num += _knightly_number(n, m-1, new_kr, new_kc, pr, pc, memo)

  memo[(m, kr, kc)] = knightly_num
  return knightly_num

def is_inbounds(n, r, c):
  row_inbounds = 0 <= r < n
  col_inbounds = 0 <= c < n
  return row_inbounds and col_inbounds