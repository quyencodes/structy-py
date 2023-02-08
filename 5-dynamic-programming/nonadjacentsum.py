def main():
  pass

class Solution:
  def non_adjacent_sum(self, nums):
    memo = {}
    return self._non_adjacent_sum(nums, 0, memo)

  def _non_adjacent_sum(self, nums, i, memo):
    if i in memo:
      return memo[i]

    if i >= len(nums):
      return 0

    include = nums[i] + non_adjacent_sum(nums, i + 2, memo)
    exclude = non_adjacent_sum(nums, i + 1, memo)

    memo[i] = max(include, exclude)
    return memo[i]


if __name__ == "__main__":
  main()
