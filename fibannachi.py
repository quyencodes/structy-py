# sum of the last 2 numbers

# recursive approach
# def fibannachi(num):
#   # base case
#   if num <= 1:
#     return 0

#   # base case 3
#   if num == 2:
#     return 1

#   # recursive case
#   return fibannachi(num - 1) + fibannachi(num - 2)

# def fibannachi(num):
#   total = 0

#   if num <= 1:
#     return 0
#   if num == 2:
#     return 1

#   while num >= 2:




# fibannachi(1) = 0
# fibannachi(2) = 1

# input will be non negative
# test1 = fibannachi(3)
# test1 = fibannachi(4)

# print(test1)


def fib_iterative(n):
  if n <= 1:
    return 0

  if n == 2:
    return 1

  i = 0
  j = 1

  for _ in range(2, n):
    l = i + j
    i = j
    j = l

  return l

print(fib_iterative(6))