def counting_change(amount, coins):
  memo = {}
  return coin_change(amount, coins, 0, memo)


def coin_change(amount, coins, k, memo):
  key = (k, amount)
  if key in memo:
    return memo[key]

  if amount == 0:
    return 1

  if k == len(coins):
    return 0

  total_coins = 0
  coin = coins[k]
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    total_coins += coin_change(remainder, coins, k + 1, memo)

  memo[key] = total_coins
  return total_coins
