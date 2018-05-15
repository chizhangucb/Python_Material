# Object-oriented programming (OOP) is a programming language model organized around objects rather than "actions" and data rather than logic.
# Numeric Data Types

type(2)
type(1.5)
type(1+1j)
True + True
type(-True)
1/3 == 0.333333333333333300000  # Beware of approximations
from math import pi, tan
tan(pi/4)


# Dates
# Compound objects combine objects together
# A date: a year, a month, and a day
# An abstract data type lets us manipulate compound objects as units
# Isolate two parts of any program that uses data

from datetime import date
today = date(2014, 9, 24)
freedom = date(2014, 12, 18)
str(freedom - today)
today.year
today.strftime('%A, %B %d')
type(today)

# Rational arithmetic

def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

# add_rational([1,2],[1,4])
# However, abstraction barrier too big! You cannot assume that x and y will be inputed as lists.

def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """Return whether rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational x."""
    print(numer(x), "/", denom(x))

# Pairs
# A list literal: comma-seperated expression in brackets: pair = [1, 2]
# "Unpacking" a list: x, y = pair   => x=1; y=2
# Element selection using the selection operator: pair[0] => 1;  pair[1] => 2
# Alternative way to select:
# from operator import getitem
# getitem(pair, 0)    => 1
# getitem(pair, 1)    => 2

# Constructor and selectors

def rational(n, d):
    """Construct a rational number x that represents n/d."""
    return [n, d]

def numer(x):
    """Return the numerator of rational number x."""
    return x[0]

def denom(x):
    """Return the denominator of rational number x."""
    return x[1]


# Improved constructor
# Constructors, selectors, and behavior conditions:
# Together, selectors are the inverse of the constructor

from fractions import gcd
def rational(n, d):
    """Construct a rational number x that represents n/d in lowest terms."""
    g = gcd(n, d)
    return [n//g, d//g]

# Functional pair

def pair(x, y):
    """Return a functional pair."""
    def get(i):
        if i == 0:
            return x
        elif i == 1:
            return y
    return get

def select(p, i):
    """Return the element at index i of pair p."""
    return p(i)
