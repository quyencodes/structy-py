"""
dp - problem solving technique where we break down our problems into subproblems, solve the
subproblems, use the solutions to the subproblems to other subproblems

dp - problem solving technique where we break down our problems into subproblems
solve our subproblems
use the solutions to the subproblems for other subproblems

n - len(coins)
a - amount

brute force solution:
time - o(n^a)
space - o(a)



"""


def min_change(amount, coins):
  res = _min_change(amount, coins, {})
  if res == float("+inf"):
    return -1
  else:
    return res


def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]

  if amount < 0:
    return float("+inf")

  if amount == 0:
    return 0

  min_coins = float("+inf")
  for coin in coins:
    change = 1 + _min_change(amount - coin, coins, memo)
    min_coins = min(min_coins, change)

  memo[amount] = min_coins
  return memo[amount]
