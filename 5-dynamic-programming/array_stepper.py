def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, i, memo):
  if i in memo:
    return memo[i]

  if i >= len(numbers) - 1:
    memo[i] = True
    return memo[i]

  max_step = numbers[i]
  for step in range(1, max_step + 1):
    if _array_stepper(numbers, i + step, memo):
      return True

  memo[i] = False
  return memo[i]