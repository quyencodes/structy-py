def min_change(amount, coins):
  memo = {}
  ans = _min_change(amount, coins, memo)
  if ans == float("inf"):
    return -1
  else:
    return ans

def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]

  if amount == 0:
    return 0

  min_coins = float("inf")
  for coin in coins:
    new_amount = amount - coin
    if new_amount >= 0:
      num_coins = 1 + _min_change(new_amount, coins, memo)
      if num_coins < min_coins:
        min_coins = num_coins

  memo[amount] = min_coins
  return min_coins


def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]

  if amount == 0:
    return 0

  min_coins = float("inf")
  for coin in coins:
    new_amount = amount - coin
    if new_amount >= 0:
      num_coins = 1 + _min_change(new_amount, coins)
      if num_coins < min_coins:
        min_coins = num_coins

  memo[amount] = min_coins
  return min_coins