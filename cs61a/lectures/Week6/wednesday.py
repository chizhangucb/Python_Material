################
# Linked lists #
################

# Lecture 13

empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]

# We can implement linked lists as pairs. We'll use two-element lists to represent pairs.

### +++ === ABSTRACTION BARRIER === +++ ###

# Recursive list examples

four = link(1, link(2, link(3, link(4, empty))))
march = link(1, link(2, link(1, link(2, empty))))
both = link(march, link(four, empty))

# Which of these evaluates to 3?  (First one)
# first(rest(rest(first(rest(both)))))
# first(rest(first(rest(rest(both)))))
# first(rest(first(rest(first(both)))))
# first(rest(rest(rest(first(both)))))
# first(first(rest(rest(first(both)))))


# Implementing the sequence abstraction

def len_link(s):
    """Return the length of linked list s.

    >>> len_link(four)
    4
    >>> len_link(both)
    2
    """
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Return the element at index i of linked list s.

    >>> getitem_link(march, 3)
    2
    """
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


# Recursive implementation

def len_link_recursive(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)

s = link( 3, link(1, link(4, empty)))
at_index_two = getitem_link(s, 2)

# Manipulating linked lists

def extend(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend(rest(s), t))

def reverse(s):
    """Return s reversed.

    >>> r = link(4, link(3, link(2, link(1, empty))))
    >>> reverse(four) == r
    True
    """
    return reverse_to(s, empty)

def reverse_to(s, result):
    if s == empty:
        return result
    else:
        return reverse_to(rest(s), link(first(s), result))

def apply_to_all_link(f, s):
    """Apply f to each element of s.

    >>> apply_to_all_link(lambda x: x*x, four)
    [1, [4, [9, [16, 'empty']]]]
    """
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))


# Partitioning numbers

def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty) # A list containing the empty partition
    elif n < 0:
        return empty
    elif m == 0:
        return empty
    else:
        # Do I use at least one m?
        yes = partitions(n-m, m)
        no = partitions(n, m-1)
        add_m = lambda s: link(m, s)
        yes = apply_to_all_link(add_m, yes)
        return extend(yes, no)

def join(s, separator):
    """Return a string of all elements in s separated by separator.

    >>> join(four, ", ")
    '1, 2, 3, 4'
    """
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join(rest(s), separator)

def print_partitions(n, m):
    """Print the partitions of n using parts of up to m.

    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join(s, " + "), lists)
    print(join(strings, "\n")) # seperate by adding a new line


################
# Rooted trees #
################

# A rooted tree has a root value and a sequence of branches, which are rooted trees.
# A rooted tree with zero branched called a leaf
# The rooted values of sub-trees within a rooted tree are often called node values or nodes.

def rooted(value, branches):
    for branch in branches:
        assert is_rooted(branch), 'branches must be rooted trees'
    return [value] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_rooted(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_rooted(branch):
            return False
    return True

### +++ === ABSTRACTION BARRIER === +++ ###

def fib_tree(n):
    """Construct a Fibonacci tree.

    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    """
    if n == 0 or n == 1:
        return rooted(n, [])
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        root_value = root(left) + root(right)
        return rooted(root_value, [left, right])

def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m.

    >>> partition_tree(2, 2)
    [2, [True], [1, [1, [True], [False]], [False]]]
    """
    if n == 0:
        return rooted(True, [])
    elif n < 0:
        return rooted(False, [])
    elif m == 0:
        return rooted(False, [])
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return rooted(m, [left, right])

def print_partitions(tree, partition = empty):
    if branch(tree) = [] and root(tree):
        print(join[partittion, " + "]}
    elif branches(tree):
        m = root(tree)
        left, right = branches(tree)
        print_partitions(left, link(m, partition))
        print_partitions(right, partition)

def print_parts(tree, partition=empty):
    """Print the partitions encoded in a partition tree.

    >>> print_parts(partition_tree(6, 4))
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    if not branches(tree) and root(tree):
        print(join(reverse(partition), ' + '))
    elif branches(tree):
        left, right = branches(tree)
        m = root(tree)
        print_parts(left, link(m, partition))
        print_parts(right, partition)

# Representing strings: UTF-8 Encoding
# UTF (UCS (Univesal Character set) Tranformation Format)
# Unicode: Correspondence between characters and integers.
# UTF-8: Correspondence between those integers and bytes
# A byte is 8 bits and can encode any integer 0-255.
# Variable-length encoding: integers vary in teh number of bytes required to encode them.
# string length is measured in characters, bytes length in bytes

def string_encoding_demos():
    ord("A")   # 65
    hex(ord('A'))
    print('\a')
    print('1\n2\n3')
    from unicodedata import lookup, name
    name('A')
    lookup('WHITE FROWNING FACE')
    lookup('SNOWMAN')
    lookup('SNOWMAN') + ' hello snowman'
    lookup('SOCCER BALL')
    lookup('BABY')
    s = lookup('SNOWMAN')
    s.encode('utf-8') # b'\xe2\x98\x83' => it takes 3 bytes to encode
    len(s.encode('utf-8'))  # 3
    len('A')
    'A'.encode()
    frown = lookup('WHITE FROWNING FACE')
    len(frown)
    len(frown.encode())
    dir('')
    "hello".capitalize()  # "Hello"
    "hello".upper()       # "HELLO"
