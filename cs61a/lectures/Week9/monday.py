"""Lecture 21 examples"""

# Properties of Orders of Growth
# Constants: do not affect the order of growth of a process
# Logarithm: the base of logarithm does not affect the order of growth of a process
# Nesting: when an inner process is repeated for each step in an outer process, multiply
# the steps in the outer and inner process to find the total number of steps.

# Examples (n is the problem size):
"""The most important ones are exp, linear and log growth"""
# 1. Exponential growth theta(b^n) where b is a constant. Recursive fib does
# 2. Quadratic growth theta(n^2). Function overlap does
# 3. Linear growth theta(n). Eg. slower factors or exp
# 4. Logarithmic growth theta(log(n)). Eg. fast exp  (Very efficient)
# 5. Constant theta(1). The problem size doesn't matter.

# Time

def count(f):
    """Return a counted version of f with a call_count attribute.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.call_count
    21891
    """
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

from math import sqrt

def divides(k, n):
    """Return whether k evenly divides n."""
    return n % k == 0

def factors(n):
    """Count the positive integers that evenly divide n.

    >>> factors(576)
    21
    """
    total = 0
    for k in range(1, n+1):
        if divides(k, n):
            total += 1
    return total

def factors_fast(n):
    """Count the positive integers that evenly divide n.

    >>> factors_fast(576)
    21
    """
    sqrt_n = sqrt(n)
    k, total = 1, 0
    while k < sqrt_n:
        if divides(k, n):
            total += 2
        k += 1
    if k * k == n:
        total += 1
    return total
            
# Space
# Which environment frames do we need to keep during evaluation
# At any moment there is a set of active environments
# Values and frames in active environment consume memoery
# Active environment: for any function calls currently being evaluated.
# Parent environments of functions named in active environments

def count_frames(f):
    """Return a counted version of f with a max_count attribute.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count_frames(fib)
    >>> fib(20)
    6765
    >>> fib.open_count
    0
    >>> fib.max_count
    20
    >>> fib(25)
    75025
    >>> fib.max_count
    25
    """
    def counted(n):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

def factors_rec(n, k=1):
    """Count the positive integers >= k that evenly divide n.

    >>> factors_rec(576)
    21
    """
    if k > sqrt(n):
        return 0
    elif k == sqrt(n):
        return 1
    elif divides(k, n):
        return 2 + factors_rec(n, k+1)
    else:
        return factors_rec(n, k+1)

def fib(n):
    """The nth Fibonacci number.

    >>> fib(20)
    6765
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

# Exponentiation

def exp(b, n):
    """Return b to the n.

    >>> exp(2, 10)
    1024
    """
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)

def square(x):
    return x*x

def exp_fast(b, n):
    """Return b to the n.

    >>> exp_fast(2, 10)
    1024
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)

# Overlap

def overlap(a, b):
    """Count the number of items that appear in both a and b.
    # If a and b are both length n, then overlap takes theta(n^2) steps.

    >>> overlap([1, 3, 2, 2, 5, 1], [5, 4, 2])
    3
    """
    count = 0
    for item in a:
        if item in b:
            count += 1
    return count
