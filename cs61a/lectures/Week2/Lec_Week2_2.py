#### High-Order Functions
# ## Fibonacci numbers
def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 1, 0   # Fibonacci numbers 1 and 2
    k = 0               # Which Fib number is curr?
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

fib(2)  # 1
fib(3)  # 2

def fib_alt_test():
    assert fib_alt(2) == 1, 'The 2nd Fibonacci number should be 1'
    assert fib_alt(3) == 1, 'The 3rd Fibonacci number should be 1'
    assert fib_alt(50) == 7778742049, 'Error at the 50th Fibonacci number'

def fib_alt(n):
    """Compute the nth Fibonacci number, for n >= 2.
    >>> fib_alt(8) == 13
    True
    >>> fib_alt_test()

    """
    pred, curr = 0, 1   # Fibonacci numbers 1 and 2
    k = 2               # Which Fib number is curr?
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

fib_alt(2)  # 1
fib_alt(3)  # 1

## Functions as General Methods
# The golden ratio, often called "phi", is a number near 1.6 that
# appears frequently in nature, art, and architecture.
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

improve(golden_update, square_close_to_successor)

from math import sqrt
phi = 1/2 + sqrt(5)/2

def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'

improve_test()


## Regular geometric shapes relate length and area.

from math import pi, sqrt

def area_square(r):
    """Return the area of a square with side length R."""
    assert r > 0, "A length must be positive"
    return r * r

def area_circle(r):
    """Return the area of a circle with radius R."""
    return r * r * pi

def area_hexagon(r):
    """Return the area of a regular hexagon with side length R."""
    return r * r * 3 * sqrt(3) / 2

def area(r, shape_constant):
    """Return the area of a shape from length measurement R."""
    assert r > 0, "A length must be positive"
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)

area_hexagon(-10)

## Testing
def sum_naturals(n):
    """Return the sum of the first n natural numbers.

    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050

    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

from doctest import testmod
testmod()

from doctest import run_docstring_examples
run_docstring_examples(sum_naturals, globals(), True)
run_docstring_examples(fib_alt, globals(), True)

# When writing Python in files, all doctests in a file can be run
# by starting Python with the doctest command line option:
# python3 -m doctest <python_source_file>

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)

from operator import mul

def pi_term(k):
    return 8 / mul(k * 4 - 3, k * 4 - 1)

summation(10e5, pi_term)


## Call Expression as Operator Expressions
def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return(x)

def g(y):
    return (y + 5) // 3

result = repeat(g, 5)

def make_adder(n):
    def adder(k):
        return k + n
    return adder

add_three = make_adder(3)
add_three
add_three(4)
make_adder(2000)(13)

## Lambda Expression
# Lambda key word introduces a function with
# 1. formal parameter x that returns the value of "x * x"
# 2. No "return" keyword
# 3. Must be a single expression (so a simple function)
# 4. Only the def statement gives the function an intrinsic name,
# but otherwise lambda behaves like any other function.
square = lambda x: x * x
square
square(10)
(lambda x: x * x)(3)