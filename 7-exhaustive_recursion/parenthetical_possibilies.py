"""
base case:
if len(s) == 0: return ['']

recursive case:

Base case: If len(s) == 0: return [""]. If no open bracket, iterate through recursive call and add self to the beginning of each result in the list. If there is an open bracket, get the substring from open to closing. Iterate through the group and add it to the recursive call.

If we don't see an open bracket '(', iterate through the recursive call and add self to the beginning of each subresult. If we do see an open bracket,

"""


def parenthetical_possibilities(s):
  if len(s) == 0:
    return ['']

  first = s[0]
  all_possibilities = []

  if first.startswith('('):  # if we have a group
    closing = s.index(')')
    group = s[1:closing]
    # print(group)
    for letter in group:
      sub_possibilities = parenthetical_possibilities(s[closing + 1:])
      for sub in sub_possibilities:
        all_possibilities.append(letter + sub)
  else:  # if we don't have a group, just letter
    possibilities = parenthetical_possibilities(s[1:])
    for subresult in possibilities:
      all_possibilities.append(first + subresult)

  return all_possibilities
