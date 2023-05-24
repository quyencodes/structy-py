"""
dp - problem solving technique where we break up our problem into subproblems, solve our subproblems,
use the solutions we gathered from the subproblems to other subproblems

nodes - sub problems
edges - decisions we make

base cases:
if amount == 0: return 1
if amount < 0: return float("inf")

recursive cases:
1. iterate through the coins
2. choose 1 + min(recursive cases)
3. memoize

time: o(c**a), where c is the len(coins) and a is the amount
space: o(a)

optimized:
time: o(a*c)
space: o(a)
"""


def min_change(amount, coins):
  attempt = _min_change(amount, coins, {})
  if attempt == float('inf'):
    return -1
  else:
    return attempt

def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]

  if amount < 0:
    return float("inf")

  if amount == 0:
    return 0

  min_coins = float("inf")
  for coin in coins:
    num_coins = 1 + _min_change(amount - coin, coins, memo)
    min_coins = min(min_coins, num_coins)

  memo[amount] = min_coins
  return min_coins




