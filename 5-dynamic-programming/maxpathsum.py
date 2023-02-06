
def productExceptSelf(nums):
  res = [1 for i in range(len(nums))]
  prefix = 1
  for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]

  print(res)
  postfix = 1
  for j in range(len(nums) - 1, -1, -1):
    res[j] *= postfix
    postfix *= nums[j]

  return res

print(productExceptSelf([1, 2, 3, 4]))