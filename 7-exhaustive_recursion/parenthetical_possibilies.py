def parenthetical_possibilities(s):
  if len(s) == 0:
    return ['']

  choices, remainder = get_choices(s)

  all_possibilities = []
  for choice in choices:
    sub_possibilities = parenthetical_possibilities(remainder)
    for possibility in sub_possibilities:
      all_possibilities.append(choice + possibility)

  return all_possibilities

def get_choices(s):
  first = s[0]
  if s[0] == '(':
    end = s.index(')')
    group = s[1:end]
    remaining = s[end+1:]
    return (group, remaining)
  else:
    return (s[0], s[1:])