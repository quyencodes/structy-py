def token_replace(s, tokens):
    res = ''
    i, j = 0, 1
    while i < len(s):
        if s[i] != '$':
            res += s[i]
            i += 1
            j = i + 1
        elif s[j] != '$':
            j += 1
        else:
            key = s[i:j + 1]
            word = tokens[key]
            res += word
            i = j + 1
            j = i + 1

    return res


tokens = {
    '$LOCATION$': 'park',
    '$ANIMAL$': 'dog',
}
print(token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens))
