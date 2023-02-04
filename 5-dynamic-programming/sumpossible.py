def sum_possible(amount, numbers, memo={}):
  if amount in memo:
    return memo[amount]

  if amount == 0:
    return True

  for num in numbers:
    target = amount - num
    if target >= 0:
      memo[target] = sum_possible(target, numbers)
      if memo[target] == True:
        return True

  return False