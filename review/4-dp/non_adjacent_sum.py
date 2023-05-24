"""
dp - problem solving technique where we:
1. break down our problem into subproblems
2. solve our subproblems
3. reuse the solutions to solve other subproblems

base cases:
- when list is empty, return 0

recursive cases:
- include the first number
- dont include the first number
- recursively go through the other non-adjacent numbers

brute force:
time - o(2**n)
space - o(n)

optimal:
time - o(n)
space - o(n)

"""

def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, {}, 0)

def _non_adjacent_sum(nums, memo, i):
  # key = tuple(nums)

  if i in memo:
    return memo[i]

  if len(nums) <= i:
    return 0

  include = nums[i] + _non_adjacent_sum(nums, memo, i+2)
  exclude = _non_adjacent_sum(nums, memo, i+1)

  memo[i] = max(include, exclude)
  return max(include, exclude)




