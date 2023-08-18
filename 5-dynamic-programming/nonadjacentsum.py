"""
dp - problem solving technique where
1) we break down our problems into subproblems
2) we solve our subproblems
3) we reuse our solutions to our subproblems for other subproblems (memoization)

nodes - subproblems
edges - decisions we take

base cases:
1. size of list

recursive cases:
1. take the first number and copy the list from list[2:]
2. recurse the list[1:]

                              [2, 4, 5, 12, 7]
                              /              \
                      [5, 12, 7]           [4, 5, 12, 7]
                      /       \             /         \
                  [7]        [12, 7]    [12, 7]      [5, 12, 7]
                  /            /  \      /     \      /       \
                []           []   [7]  []      [7]  [7]       [12, 7]
                                  /                            /    \
                                 []                           []     [7]
                                                                     /
                                                                    []
"""


def non_adjacent_sum(nums):
  memo = {}
  return _njs(nums, memo)


def _njs(nums, memo):
  key = tuple(nums)
  if key in memo:
    return memo[key]

  if len(nums) == 0:
    return 0

  if len(nums) == 1:
    return nums[0]

  first = nums[0]
  with_first = first + _njs(nums[2:], memo)
  without_first = _njs(nums[1:], memo)

  memo[key] = max(with_first, without_first)
  return memo[key]
