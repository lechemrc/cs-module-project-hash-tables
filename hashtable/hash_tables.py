# Lecture notes

my_arr = ['hi', 'world', 'how', 'are', 'you', 'lorem', 'ipsum', 'set']

# Search for an element in this array
## O(n) -- linear search
def find_element(arr, el):
    for thing in arr:
        if thing == el:
            return True
    return False

# Or if we sorted, binary search! 
## O(log n)

# Which big ) complexities are faster than log n?
## Constant time: O(1)
### If we increase the input, we still take number of steps to find what we're looking for

# def magic_func_find_index(arr, el):
#     return el_index

# idx = magic_func_find_index(my_arr, 'set') # 7
# my_arr[idx] # ta-da

# Hash tables == arrays + hashing function: O(1)

# Wrtie a function that will take a string and return a number
def len_hash(my_str):
    return len(my_str)
# This has lots of collisions
len('was') == len('sad')
len('bats') == len('hats')
# Fast to create
# Deterministic 

## We could map letters to numbers, but that's already done
# ASCII was the first mapping of letters to numbers
## UTF-8 is ASCII on steroids, designed to work with ASCII but be universal
## use .encode()

## a: 1
## b: 2
 
def UTF8_hash(my_str):
    # for letter in str:
        # val = ord(letter)
        # total += val
    total = 0
    utf_bytes = my_str.encode()
    for byte in utf_bytes:
        total += byte

    return total

print(UTF8_hash('sad'))
print(UTF8_hash('was'))
# ...but we will still have collisions 

# A hash function: takes str, gives back num
## Operate on bytes that make up str
## Deterministic

# To improve our hash functions, make output more unique!
## SHA256

# Hash function + array! 
## How to map the output of our hash function to an index in an array? 

