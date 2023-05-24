def tribonacci(n):
  if n == 1 or n == 0:
    return 0

  if n == 2:
    return 1

  return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)