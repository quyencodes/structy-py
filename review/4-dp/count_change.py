"""
dp - ps technique where we:
1. break down our problems into subproblems
2. solve the subproblems
3. reuse the solutions we got from the subproblems to our other problems

nodes - subproblems
edges - decisions we make
"""

def counting_change(amount, coins):
  return _counting_change(amount, coins, {})

def _counting_change(amount, coins, memo):
  if amount < 0:
    return 0

  if amount == 0:
    return 1

  amt = 0
  for coin in coins:
    new_amount = amount - coin
    amt += counting_change(new_amount, coins)

  return amt


