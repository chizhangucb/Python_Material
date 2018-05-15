"""Lecture 23 examples"""

# Link, Tree, and BinaryTree classes

class Link:
    """A linked list."""

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

class BinaryTree(Tree):
    """A tree with exactly two branches, which may be empty."""
    empty = Tree(None)
    empty.is_empty = True

    def __init__(self, entry, left=empty, right=empty):
        for branch in (left, right):
            assert isinstance(branch, BinaryTree) or branch.is_empty
        Tree.__init__(self, entry, (left, right))
        self.is_empty = False

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def __repr__(self):
        if self.left.is_empty and self.right.is_empty:
            return 'Bin({0})'.format(self.entry)
        elif self.right.is_empty:
            return 'Bin({0}, {1})'.format(self.entry, self.left)
        else:
            left = 'Bin.empty' if self.left.is_empty else repr(self.left)
            return 'Bin({0}, {1}, {2})'.format(self.entry, left, self.right)

Bin = BinaryTree

# List processing functions

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


# Cycles

def cycle_demo():
    """A linked list can contain cycles.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first = 5
    >>> t = s.rest
    >>> t.rest = s
    >>> s.first
    5
    >>> s.rest.rest.rest.rest.rest.first
    2
    """

# Hailstones

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

def is_int(x):
    return int(x) == x

def is_odd(n):
    return n % 2 == 1

def hailstone_tree(length, n=1):
    """Build a tree in which paths are hailstone sequences.

    >>> hailstone_tree(6)
    Tree(1, [Tree(2, [Tree(4, [Tree(8, [Tree(16, [Tree(32), Tree(5)])])])])])
     """
    if length == 1:
        return Tree(n)
    else:
        above, below = 2*n, (n-1)/3
        branches = [hailstone_tree(length-1, above)]
        if below > 1 and is_int(below) and is_odd(below):
            branches.append(hailstone_tree(length-1, int(below)))
        return Tree(n, branches)

def leaves(tree):
    """Return the leaves of a Tree.

    >>> leaves(hailstone_tree(7))
    [64, 10]
    >>> leaves(hailstone_tree(8))
    [128, 21, 20, 3]
    >>> leaves(hailstone_tree(12))
    [2048, 341, 340, 336, 320, 53, 52, 48]
    """
    if not tree.branches:
        return [tree.entry]
    else:
        branch_leaves = apply_to_all(leaves, tree.branches)
        return reduce(add, branch_leaves, [])

def hailstone_bin(length, n=1):
    """Build a BinaryTree in which paths are hailstone sequences.

    >>> hailstone_bin(3)
    Bin(1, Bin(2, Bin(4)))
    >>> hailstone_bin(6)
    Bin(1, Bin(2, Bin(4, Bin(8, Bin(16, Bin(32), Bin(5))))))
    """
    if length == 1:
        return Bin(n)
    else:
        above, below = 2*n, (n-1)/3
        left = hailstone_bin(length-1, above)
        right = Bin.empty
        if below > 1 and is_int(below) and is_odd(below):
            right = hailstone_bin(length-1, int(below))
        return Bin(n, left, right)
d
def longest_path_below(k, t):
    """Return the longest path through t of entries all less than k.

    >>> longest_path_below(20, hailstone_bin(10))
    [1, 2, 4, 8, 16, 5, 10, 3, 6, 12]
    >>> longest_path_below(100, hailstone_bin(25))
    [1, 2, 4, 8, 16, 5, 10, 20, 40, 13, 26, 52, 17, 34, 11, 22, 44, 88, 29, 58, 19, 38, 76, 25, 50]
    """
    if t.is_empty:
        return []
    elif t.entry >= k:
        return []
    else:
        left = longest_path_below(k, t.left)
        right = longest_path_below(k, t.right)
        if len(left) > len(right):
            return [t.entry] + left
        else:
            return [t.entry] + right

def oski(bear):
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [berk+1, berk-1]
        bear = lambda ley: berk - ley
        return [berk, cal(berk)]
    return cal(2)
oski(abs)
