def substitute_synonyms(sentence, synonyms):
  if len(sentence) == 0:
    return ['']

  choices, remainder = get_choices(sentence, synonyms)

  res = []
  for choice in choices:
    remaining_sentence = substitute_synonyms(remainder, synonyms)
    for sentence in remaining_sentence:
      temp = choice + ' ' + sentence if sentence != '' else choice
      res.append(temp)
  return res

def get_choices(sentence, synonyms):
  words = sentence.split()
  first_word = words[0]

  if first_word in synonyms:
    other_words = synonyms[first_word]
    return (other_words, ' '.join(words[1:]))
  else:
    return ([first_word], ' '.join(words[1:]))

sentence = "road"
synonyms = {
  "follow": ["chase", "pursue"],
  "yellow": ["gold", "amber", "lemon"],
}
print(get_choices(sentence, synonyms))