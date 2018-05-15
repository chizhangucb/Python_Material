# Lists are sequences

# The sequence abstraction is a collection of behaviors:
# 1. length. A sequence has a finite length
# 2. Element selection: element corresponding to any non-negative integer index less than its length, starting at 0.
# A list is a kind of built-in sequence.

odds = [41, 43, 47, 49]
len(odds)
odds[1]
odds[0] * odds[3] + len(odds)
odds[odds[3]-odds[2]]


# For statements

digits = [1, 8, 2, 8]

def count_while(s, value):
    """Count the number of occurrences of value in sequence s.

    >>> count_while(digits, 8)
    2
    """
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total += 1
        index += 1
    return total

def count_for(s, value):
    """Count the number of occurrences of value in sequence s.

    >>> count_for(digits, 8)
    2
    """
    total = 0
    for elem in s:
    # The name elem bound in the first frame of the current environment (not a new frame)
        if elem == value:
            total = total + 1
    return total


def count_same(pairs):
    """Return how many pairs have the same element repeated.

    >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
    >>> count_same(pairs)
    2
    """
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count = same_count + 1
    return same_count


# Ranges

list(range(-2, 2)) # [-2, -1, 0, 1]
list(range(5, 8)) # [5, 6, 7]
list(range(4)) # [0, 1, 2, 3]
0 in range(-2, 2) # True
len(range(4))

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for _ in range(3):
        print('Go Bears!')


# List comprehensions

odds = [1, 3, 5, 7, 9]
[x+1 for x in odds]
[x for x in odds if 25 % x == 0]

def divisors(n):
    """Return the integers that evenly divide n.

    >>> divisors(1)
    [1]
    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    >>> [n for n in range(1, 1000) if sum(divisors(n)) == n]
    [1, 6, 28, 496]
    """
    return [1] + [x for x in range(2, n) if n % x == 0]


# Higher-order functions
# map and filter are build into Python but they don't return lists
# reduce is in the standard library in a module called functools

from operator import add, mul

def apply_to_all(map_fn, s):
    """Apply map_fn to each element of s.

    >>> apply_to_all(lambda x: x*3, range(5))
    [0, 3, 6, 9, 12]
    """
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    """List all elements x of s for which filter_fn(x) is true.

    >>> keep_if(lambda x: x>5, range(10))
    [6, 7, 8, 9]
    """
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    """Combine elements of s pairwise using reduce_fn, starting with initial.

    E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8).

    >>> reduce(mul, [2, 4, 8], 1)
    64
    """
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    """Return whether N is a perfect number.

    >>> keep_if(perfect, range(1, 1000))
    [1, 6, 28, 496]
    """
    return sum_of_divisors(n) == n
