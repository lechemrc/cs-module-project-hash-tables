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

print(UTF8_hash('supercalifragilisticexpialidocious'))
# ...but we will still have collisions 

# A hash function: takes str, gives back num
## Operate on bytes that make up str
## Deterministic

# To improve our hash functions, make output more unique!
## SHA256

# Hash function + array! 
## How to map the output of our hash function to an index in an array? 

# Doesn't work
# my_arr2 = [None] * 20
# idx = UTF8_hash('supercalifragilisticexpialidocious') # 3643
# my_arr2[idx] = 'Mary Poppins'

# How do we turn result of has function into usable index?
## Modulo (%, returns remainder) the hash with len(my_arr2)

# 1 % 20 --> 1
# 15 % 20 --> 15
# 20 % 20 --> 0
# 21 % 20 --> 1
# 22 % 20 --> 2
# 39 % 20 --> 19
# 40 % 20 --> 0

# Use modulo with hash to return a usable index
## We can now combine hash function and array

# 'put' into our array
my_arr2 = [None] * 20
my_hash = UTF8_hash('supercalifragilisticexpialidocious') # 3643
idx = my_hash % len(my_arr2)
my_arr2[idx] = 'Mary Poppins'
print(my_arr2)

# 'get' 
our_hash = UTF8_hash('supercalifragilisticexpialidocious')
idx = our_hash % len(my_arr2)

# print(my_arr2[3])
val = my_arr2[idx]
print(val)

## Key : Value pair
# 'supercalifragilisticexpialidocious' is the key
# 'Mary Poppins' is the value