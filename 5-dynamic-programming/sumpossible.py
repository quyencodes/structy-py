"""
dp - problem solving technique where we solve our subproblems,
save the solutions to the subproblems, and solve other subproblems

base case:
1. bring the amount down
2. if the amount is less than 0 return False
3. keep going down if greater than 0
4. if 0 return True


"""


def sum_possible(amount, numbers):
  memo = {}
  return _sum_possible(amount, numbers, memo)


def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]

  if amount < 0:
    return False

  if amount == 0:
    return True

  for num in numbers:
    temp = amount - num
    if _sum_possible(temp, numbers, memo):
      memo[amount] = True
      return memo[amount]

  memo[amount] = False
  return memo[amount]
