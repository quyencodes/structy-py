# input - number
# output - boolean determining if a prime number or not
# constraints - none
# edge cases - none (assume all input numbers is positive integer)

# third attempt (most optimal solution)
from math import sqrt, floor
def is_prime(n):
  if n == 1:
    return False

  for i in range(2, floor(sqrt(max)) + 1):
    if max % i == 0:
      return False

  return True

# second attempt
def is_prime(n):
  if n == 1:
    return True

  for i in range(2, n):
    if n % i == 0:
      return False

  return True

# first attempt
def is_prime(n):
  # edge case
  if n == 1:
    return False

  # iterate from 2 to n (exclusive)
  for num in range(2, n):
    true_division = n / num
    if str(true_division)[-2:] == '.0':
      return False

  return True

# time complexity
# n = input number
# time - linear o(n)
# space - constant o(1)

# better time complexity
# check factors up to sqrt(n) only
# because every factor has a corresponding pair
# when both factors point at the same number, it serves as the middle of the inflexion point of factor pairs
# time - constant o(sqrt(n))
# space - constant o(1)

is_prime(4)

# https://stackoverflow.com/questions/385325/dropping-trailing-0-from-floats