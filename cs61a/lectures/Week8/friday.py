"""Lecture 20 examples"""

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)

def count(f):
    """Return a counted version of f with a call_count attribute.

    >>> def fib(n):
    ...     if n == 1:
    ...         return 0
    ...     if n == 2:
    ...         return 1
    ...     return fib(n-2) + fib(n-1)
    >>> fib = count(fib)
    >>> fib(20)
    4181
    >>> fib.call_count
    13529
    """
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

def memo(f):
    """Memoize f.

    >>> def fib(n):
    ...     if n == 1:
    ...         return 0
    ...     if n == 2:
    ...         return 1
    ...     return fib(n-2) + fib(n-1)
    >>> counted_fib = count(fib)
    >>> fib  = memo(counted_fib)
    >>> fib(20)
    4181
    >>> counted_fib.call_count
    20
    >>> fib(35)
    5702887
    >>> counted_fib.call_count
    35
    """
    cache = {}
    # To store data with cache
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> len(s)
    4
    >>> s[2]
    3
    >>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

class Tree:
    """A tree with entry as its root value."""
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

def fib_tree(n):
    """A Fibonacci tree.

    >>> fib_tree(4)
    Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    """
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.entry + right.entry, (left, right))

thirty = fib_tree(30)
thirty.entry
thirty.branches[0].entry is thirty.branches[1].branches[1].entry

def print_leaves(tree):
    """Print the entries of a tree that have no branches.
    
    >>> print_leaves(fib_tree(4))
    0
    1
    1
    0
    1
    """
    if not tree.branches:
        print(tree.entry)
    else:
        for branch in tree.branches:
            print_leaves(branch)

####################### 
# Example: Hailstones #
#######################

def hailstone(n):
    """Print a hailstone sequence and return its length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(3*n+1)

def hailstone_tree(depth, n=1):
    """Build a tree in which paths are hailstone sequences.

    >>> hailstone_tree(6)
    Tree(1, [Tree(2, [Tree(4, [Tree(8, [Tree(16, [Tree(32), Tree(5)])])])])])
    >>> print_leaves(hailstone_tree(7))
    64
    10
    >>> print_leaves(hailstone_tree(8))
    128
    21
    20
    3
    """
    if depth == 1:
        return Tree(n)
    else:
        branches = [hailstone_tree(depth-1, 2*n)]
        if n > 4 and (n-1)%3 == 0:
            branches.append(hailstone_tree(depth-1, (n-1)//3))
        return Tree(n, branches)
            
