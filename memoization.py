# Pattern Matching

## Data structures
### Algorithms operate on data
### Consider your data structure: tree, array, hash table?

## Time complexity
### Easy to think about with arrays vs hash tables

# When to use Hash Tables

## Problem they solve: we have something we need to look up quickly
### especially where slower methods would cause a problem

my_arr = [1, 2, 3, 4]
my_hash_table = {}
def linear_search(arr, el):
    # check hash table first
    for thing in arr:
        if thing == el:
            my_hash_table[el] = True
            return True
    return False

has_3_in_arr = linear_search(my_arr, 3)

# million things in arr * million lookups

# use hash tables anywhere reacquiring info would be too slow

# Memoization
## Dynamic Programming

### code up a function

### Make a function that will return the n-th element in the Fibonacci sequence

### UPER
### Polya's "How to Solve It"
### "run, right, fast"

#### Understand
##### ELI5 / Feynman Technique

##### Fib sequence?
##### 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
### Agile sprint
### Features --> cards on Kanban board --> "make a button"

##### n-th element?
### like in an array

#### Plan
##### When you have pseudocode that you can execute

### Use a recursive solution (find n-1 and n-2 things)
### Base case
#### 0 and/or 1
### Function calls itself
### Progress toward base case
#### return fib of n-1 and fib of n-2, summed

### edge cases: negative numbers and fractions not allowed

#### Execute
##### if you discover an edge case or something, throw it in your plan
def fibonacci(n):
    ### Base case
    #### 0 and/or 1
    if n <= 1:
        return n
    ### Progress toward base case
    #### return fib of n-1 and fib of n-2, summed

    return fibonacci(n-1) + fibonacci(n-2)

#### Review
# fibonacci(3) # should return 2
# fibonacci(2) # should return 1

# print(fibonacci(45))

#### What is the time complexity of this function?
##### Linear?? only if recursive function calls itself once
##### c^n, c**n, 2^n

### Talk about recursion
#### O(1)
#### O(log n)
#### O(n)
#### O(n log n)
#### O(n^c), O(n^2), O(n^3), O(n^4)
#### O(c^n), O(2^n) Exponential

### Improve time complexity of our function using memoization
#### make not exponential!


memo = {}
def memoized_fibonacci(n):
    ### Base case
    #### 0 and/or 1
    if n <= 1:
        return n

    ### check if we have a result before doing the computation
    if n in memo:
        return memo[n]
    
    ### store results as we go
    else:
    ### Progress toward base case
    #### return fib of n-1 and fib of n-2, summed
        memo[n] = memoized_fibonacci(n-1) + memoized_fibonacci(n-2)

    return memo[n]

import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)


# print(memoized_fibonacci(1500))

## Tail call recursion


## Caching
## Lookup tables
## Sorting - can we do it with hash tables?
## Birthday paradox



import math

# resize every once in a while
my_arr = []
for i in range(10000):
    my_arr.append(i)

# pre-allocating
my_arr = [None] * 10000
for i in range(10000):
    my_arr[i] = i

# precalculate the results and cache them in a dict
cache = {}
# kind of an expensive computation
def inverse_root(x):
    return 1/math.sqrt(x)

def build_lookup_table():
    for i in range(1, 10000):
        cache[i] = inverse_root(i)
## suppose large numbers, user-facing
## how could we avoid running this computation at time of need?

build_lookup_table()

## Solves if user asks for a number we have not precalculated
## Populates lookup table
def get_inverse_root(x):
    if x in cache:
        return cache[x]
    else:
        cache[x] = inverse_root(x)
        return cache[x]

print(get_inverse_root(9999))

print(get_inverse_root(100000))