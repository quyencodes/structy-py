def parenthetical_possibilities(s):
  return _parenthetical_possibilities(s)

def _parenthetical_possibilities(s):
  if len(s) == 0:
    return ['']

  choices, remainder = get_choices(s)

  all_possibilities = []
  for choice in choices:
    remainder_possibilities = _parenthetical_possibilities(remainder)
    for possiblity in remainder_possibilities:
      all_possibilities.append(choice + possiblity)

  return all_possibilities

def get_choices(s):
  res = ''
  if s[0] == '(':
    end = s.index(')')
    choices = s[1:end]
    remainder = s[end+1:]
    return (choices, remainder)
  else:
    return (s[0], s[1:])

print(get_choices('(abc)de')) # 'abc'
print(get_choices('xyz')) # 'x'


