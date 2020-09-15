def histo(s):
    cache = {}
    drop_chars = [
        '\"', ':', ';', ',', '.', '-', '+', '=', '/', 
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

    sort_orders = sorted(cache.items(), key=lambda x: x[1], reverse=True)

    for word in sort_orders:
        print(word[0] + (' ' * (17 - len(word[0]))) + ('#' * int(word[1])))


if __name__ == "__main__":
    f = open('applications/histo/robin.txt', 'r')
    content = f.read()
    print(histo(content))
