"""
dp - problem solving technique where we break down a problem into subproblems, solve
the subproblems and reuse those solutions to the other sub problems

nodes - current sub problem
edges - decision we made

base cases:
- if amount == 0, return True
- if amount < 0, return False

recursive cases:
- use numbers in the numbersList and decrement amount

"""

def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]

  if amount < 0:
    return False

  if amount == 0:
    return True

  for num in numbers:
    attempt = _sum_possible(amount - num, numbers, memo)
    if attempt == True:
      memo[amount] = True
      return memo[amount]

  memo[amount] = False
  return memo[amount]


