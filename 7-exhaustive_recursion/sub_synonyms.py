def substitute_synonyms(sentence, synonyms):
  words = sentence.split(' ')
  subarrays = generate(words, synonyms)
  final_result = []
  for subarray in subarrays:
    final_result.append(' '.join(subarray))
  return final_result


def generate(words, synonyms):
  if len(words) == 0:
    return [[]]

  first_word = words[0]
  remaining_words = words[1:]
  subarrays = generate(remaining_words, synonyms)

  if first_word in synonyms:
    result = []
    for synonym in synonyms[first_word]:
      for subarray in subarrays:
        result.append([synonym, *subarray])
    return result
  else:
    result = []
    for subarray in subarrays:
      result.append([first_word, *subarray])
    return result

