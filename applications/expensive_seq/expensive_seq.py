cache = {}

def expensive_seq(x, y, z):
    """
     if x <= 0: y + z
     if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)
    """
    if (x, y, z) in cache:
        return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))


# -----------------------------------------------------------------------------------------
# def rot13(phrase):
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     out_phrase = ""
#     for char in phrase:
#         out_phrase += abc[(abc.find(char)+13)%26]
#     print(out_phrase.replace('m', ' '))
#     return out_phrase

# words = "Va Clguba, n qvpg xrl pna or nal vzzhgnoyr glcr... vapyhqvat n ghcyr."
# rot13(words)

###  "n  ython  a dict key can be any i  utable type    including a tuple"