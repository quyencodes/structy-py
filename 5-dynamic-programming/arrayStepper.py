def array_stepper(numbers):
  memo = {}
  return _array_stepper(numbers, 0, memo)


def _array_stepper(numbers, k, memo):
  if k in memo:
    return memo[k]

#   if k >= len(numbers):
#     return False

  if k == len(numbers) - 1:
    return True

  step = numbers[k]
  max_steps = step + 1
  for i in range(1, max_steps):
    if _array_stepper(numbers, k + i, memo):
      memo[k] = True
      return True

  memo[k] = False
  return False
