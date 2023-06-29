def max_increasing_subseq(numbers):
  return _max_increasing_subseq(numbers, 0, float('-inf'), {})

def _max_increasing_subseq(numbers, i, prev, memo):
  key = (i, prev)
  if key in memo:
    return memo[key]

  if i == len(numbers):
    return 0

  curr = numbers[i]
  options = []

  without_first = _max_increasing_subseq(numbers, i + 1, prev, memo)
  options.append(without_first)

  if prev < curr:
    with_first = 1 + _max_increasing_subseq(numbers, i + 1, curr, memo)
    options.append(with_first)

  memo[key] = max(options)
  return max(options)