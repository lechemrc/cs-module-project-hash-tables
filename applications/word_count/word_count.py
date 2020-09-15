# import string

def word_count(s):
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



# if __name__ == "__main__":
#     print(word_count(""))
#     print(word_count("Hello"))
#     print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
#     print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

x = word_count('":;,.-+=/\\|[]{}()*^&')
print(x)