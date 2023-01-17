def intersection(a, b):
  return list(set(a).intersection(b))

def intersection(a, b):
  result = []
  for num in b:
    if num in a:
      result.append(num)

  return result

def intersection(a, b):
  set_a = set(a)
  return [item for item in b if item in set_a]