"""
dp - problem solving technique where we:
1) break down our problems into subproblems
2) solve our subproblems
3) reuse our solutions to our sub problems to other sub problems

nodes - subproblems, edges - decisions we make



"""


def max_palin_subsequence(string):
  memo = {}
  return mps(string, memo)


def mps(string, memo):
  if string in memo:
    return memo[string]

  if len(string) <= 0:
    return 0

  if len(string) == 1:
    return 1

  first, last = string[0], string[-1]

  max_palin_sub = 0
  if first == last:
    max_palin_sub = max(max_palin_sub, 2 + mps(string[1:-1], memo))
  else:
    max_palin_sub = max(max_palin_sub, mps(string[1:], memo))
    max_palin_sub = max(max_palin_sub, mps(string[:-1], memo))

  memo[string] = max_palin_sub
  return memo[string]
