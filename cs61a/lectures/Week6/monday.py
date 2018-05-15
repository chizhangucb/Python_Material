# Trees

nested_list = [[1, 2], [],
               [[3, False, None],
                [4, lambda: 5]]]

# A tree is either a single value called a leaf or a sequence of trees.
# Typically, some type restriction is placed on the leaves. Eg., a tree of numbers

# A tree of integers
tree = [[1, [2], 3, []], [[4], [5, 6]], 7]

def is_leaf(tree):
    return type(tree) != list

def count_leaves(tree):
    """Count the leaves of a tree.

    >>> count_leaves(tree)
    7
    """
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in tree]
        return sum(branch_counts)

# Processing a leaf is often the base case of a tree processing function
# The recursive case often makes a recursive call on each branch and then aggregate

def apply_to_leaves(map_fn, tree):
    """Apply map_fn to all leaves of tree, constructing another tree.

    >>> five = [[1, 2], [3, [4, 5]], 6]
    >>> apply_to_leaves(lambda x: x*x, five)
    [[1, 4], [9, [16, 25]], 36]
    """
    if is_leaf(tree):
        return map_fn(tree)
    else:
        return [apply_to_leaves(map_fn, b) for b in tree]

def flatten(tree):
    """Return a list containing the leaves of tree.

    >>> flatten(tree)
    [1, 2, 3, 4, 5, 6, 7]
    """
    if is_leaf(tree):
        return [tree]
    else:
        return sum([flatten(b) for b in tree], [])

pangram = [['the', 'quick', 'brown', 'fox'],
           ['jumped', 'over', 'a', 'lazy', 'dog']]

def right_binarize(tree):
    """Return a right-branching binary tree with the structure of the input.

    >>> right_binarize([1, 2, 3, 4, 5, 6, 7])
    [1, [2, [3, [4, [5, [6, 7]]]]]]
    >>> right_binarize(pangram)
    [['the', ['quick', ['brown', 'fox']]], ['jumped', ['over', ['a', ['lazy', 'dog']]]]]
    """
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]

# Demo of the Berkeley Parser:
# http://tomato.banatao.berkeley.edu:8080/parser/parser.html 

# Dictionaries
# 1. Unordered collections of key-value pairs
# 2. A key of a dictionary CANNOT be a list or a dictionary (or any mutable type)
# 3. Two keys cannot be equal; There can be as most one value for a give key

def dict_demos():
    numerals = {'I': 1.0, 'V': 5, 'X': 10}
    numerals['X']
    numerals.values()
    list(numerals.values())
    sum(numerals.values())
    dict([(3, 9), (4, 16), (5, 25)])
    numerals.get('A', 0)
    # does not have "A", so give you the default value 0
    numerals.get('V', 0)
    # has "V", so give you 5
    {x: x*x for x in range(3,6)}
    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    {1: 2, 1: 3}
    # Cannot have the same key twice
    {1:[2, 3]}
    # Can have a sequence of list of values associated with one key
    {[1]: 2}
    {1: [2]}

digits = [1, 8, 2, 8]
123 not in digits  # False
2 in digits        # True
digits[0:2]        # [1, 8]
digits[1:]         # [8, 2, 8]
# the starting index is included, but the ending index is excluded

'curry = lambda f: lambda x: lambda y: f(x, y)'
exec('curry = lambda f: lambda x: lambda y: f(x, y)')
from operator import add
curry(add)(3)(4)

