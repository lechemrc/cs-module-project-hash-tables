# Lecture notes

my arr = ['hi', 'world', 'how', 'are', 'you', 'lorem', 'ipsum', 'set']

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

def magic_func_find_index(arr, el):
    return el_index

idx = magic_func_find_index(my_arr, 'set') # 7
my_arr[idx] # ta-da

