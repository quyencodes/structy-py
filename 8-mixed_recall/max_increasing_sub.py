def max_increasing_subseq(numbers):
  memo = {}
  return _max_increasing_subseq(numbers, 0, float('-inf'), memo)

def _max_increasing_subseq(numbers, i, prev, memo):
  key = (i, prev)
  if key in memo:
    return memo[key]

  if i == len(numbers):
    return 0

  current = numbers[i]
  options = []
  dont_take_current = _max_increasing_subseq(numbers, i + 1, prev, memo)
  options.append(dont_take_current)

  if current > prev:
    take_current = 1 + _max_increasing_subseq(numbers, i + 1, current, memo)
    options.append(take_current)

  memo[key] = max(options)
  return max(options)


