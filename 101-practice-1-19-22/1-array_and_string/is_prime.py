from math import sqrt, floor

def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False

  return True

def is_prime_optimal(n):
  for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
      return False

  return True

# we want to be inclusive
# 1 2 4 8 16 32 64