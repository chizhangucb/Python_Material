# Functional arguments

def apply_twice(f, x):
    """Return f(f(x))

    >>> apply_twice(square, 2)
    16
    >>> from math import sqrt
    >>> apply_twice(sqrt, 16)
    2.0
    """
    return f(f(x))

def square(x):
    return x * x

result = apply_twice(square, 2)

# Applying a user-defined function:
# 1. Create a new frame
# 2. Bind formal parameters (f & x) to arguments;
# 3. Execute the body: return f(f(x))

def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3

repeat(g, 5)


# Functional return values

def make_adder(n):
    """Return a function that takes one argument k and returns k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

# Every user-defined function has a parent frame(often global, not always)
# The parent of a function is the frame in which it was defined
# Every local frame has a parent frame (often global)
# The parent of a frame is the parent of the function is called.

# Lexical scope and returning functions

def f(x, y):
    return g(x)

def g(a):
    return a + y

# This expression causes an error because y is not bound in g.
# f(1, 2)

# Composition

def compose1(f, g):
    """Return a function that composes f and g.

    f, g -- functions of a single argument
    """
    def h(x):
        return f(g(x))
    return h

def triple(x):
    return 3 * x

squiple = compose1(square, triple)
# squiple(5)     # 225
tripare = compose1(triple, square)
# tripare(5)     # 75
squadder = compose1(square, make_adder(2))
# squadder(3)    # 25
# compose1(square, make_adder(2))(3)    # 25
