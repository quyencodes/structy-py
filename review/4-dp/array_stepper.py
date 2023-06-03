def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, pos, memo):
  if pos in memo:
    return memo[pos]

  if pos >= len(numbers) - 1:
    return True

  curr_pos = numbers[pos]
  for i in range(1, curr_pos + 1, 1):
    new_pos = pos + i
    if _array_stepper(numbers, new_pos, memo):
      memo[pos] = True
      return True

  memo[pos] = False
  return False

