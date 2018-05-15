## Functional arguments

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

## Nested Defintions
# 1. Every user-defined function has a parent environment / frame
# 2. The parent of a function is the frame in which it was defined
# 3. Every local frame has a parent frame
# 4. The parent of a frame is the parent of a function called

def make_adder(n):
    """Return a function that takes one argument k and returns k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

## Lexical scope and returning functions

def f(x, y):
    return g(x)

def g(a):
    return a + y

# f(1, 2)  # name 'y' is not defined
# This expression causes an error because y is not bound in g.
# Because g(a) is NOT defined within f and
# g is parent frame is the global frame, which has no "y" defined

## Composition
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def triple(x):
    return 3 * x

squiple = compose1(square, triple)
squiple(5)

tripare = compose1(triple, square)
tripare(5)

squadder = compose1(square, make_adder(2))
squadder(5)

compose1(square, make_adder(2))(3)

## Function Decorators
# special syntax to apply higher-order functions as part of executing a def statement
def trace(fn):
    """Returns a function that precedes a call to its argument with a
    print statement that outputs the argument.
    """
    def wrapped(x):
        print("->", fn, '(', x, ')')
        return fn(x)
    return wrapped

# @trace affects the execution rule for def
# As usual, the function triple is created.
# However, the name triple is not bound to this function.
# Instead, the name triple is bound to the returned function
# value of calling trace on the newly defined triple function
@trace
def triple(x):
    return 3 * x

triple(12)

# The decorator symbol @ may also be followed by a call expression