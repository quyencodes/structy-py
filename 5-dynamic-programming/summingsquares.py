"""
dp - problem solving technique where:
1. we break down our problems into subproblems
2. we solve our subproblems
3. we reuse our solutions to our subproblems to other subproblems

nodes - subproblems, edges - decisions we make

base cases:
1. n == 0

recursive cases:
1. iterate up to sqrt(12)
"""
import math


def summing_squares(n):
  memo = {}
  return _ss(n, memo)


def _ss(n, memo):
  if n in memo:
    return memo[n]

  if n < 0:
    return float("inf")

  if n == 0:
    return 0

  min_squares = float("inf")
  for i in range(1, math.floor(math.sqrt(n)) + 1):
    square = i * i
    attempt = 1 + _ss(n - square, memo)
    min_squares = min(min_squares, attempt)

  memo[n] = min_squares
  return memo[n]
