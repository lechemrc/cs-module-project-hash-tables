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