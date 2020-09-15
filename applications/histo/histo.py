def histo(s):
    cache = {}
    drop_chars = [
        '\"', '\'', ':', ';', ',', '.', '-', '+', '=', '/', 
        '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&'
        ]

    no_punc = s.lower().split()
    for chars in drop_chars:
        no_punc = [i.replace(chars, '') for i in no_punc]

    for word in no_punc: 
        if word in cache: 
            cache[word] += 1
        else: 
            cache[word] = 1

    return cache

