"""
dp - problem solving technique where we:
1. break down a problem into subproblems
2. solve the subproblems
3. reuse solutions to subproblems to other problems (memoization)

nodes - subproblems
edges - decisions we make

base case:
if n==0, return 0

recursive case:
add 1 to the recursive call to count the edges

"""
import math
def summing_squares(n, memo={}):
  if n in memo:
    return memo[n]

  if n < 0:
    return float('inf')

  if n == 0:
    return 0

  min_squares = float('inf')
  for i in range(1, math.floor(math.sqrt(n)) + 1, 1):
    square = i * i
    new_n = n - square
    num_squares = 1 + summing_squares(new_n, memo)
    min_squares = min(min_squares, num_squares)

  memo[n] = min_squares
  return min_squares
