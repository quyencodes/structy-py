function joinWords(words :string[]): string {
  let res: string = ''
  for (let i = 0; i < words.length; i++) {
    res += words[i]
  }

  return res
}

const joinWords2 = (words: string[]): string => {
  let res: string = ''
  for (let i = 0; i < words.length; i++) {
    res += words[i]
  }
  return res
}

function optimizedJoinWords(words: string[]): string {
  let res: Array<string> = []
  for (let i: number = 0; i < words.length; i++) {
    res.push(words[i])
  }
  return res.join('')
}

const optimizedJoinWordsArrowFunc = (words: string[]): string => {
  let res: string[] = []
  for (let i: number = 0; i < words.length; i++) {
    res.push(words[i])
  }
  return res.join('')
}