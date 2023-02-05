def min_change(amount, coins):
  if amount == 0:
    return 0

  min_coins = float("inf")
  for coin in coins:
    new_amount = amount - coin
    if new_amount >= 0:
      num_coins = 1 + min_change(new_amount, coins)
      if num_coins < min_coins:
        min_coins = num_coins

  return min_coins