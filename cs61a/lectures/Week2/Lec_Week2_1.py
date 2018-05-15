# Readings
# http://composingprograms.com/pages/15-control.html

# An environment is a sequence of frames.
# 1. The global frame alone
# 2. A local, then the global frame

## Print
-2
print(-2)
'Go Bears'
print('Go Bears')
print(1, 2, 3)
None
print(None)
x = -2
x
x = print(-2)
x
print(print(1), print(2))

## Addition/Multiplication
2 + 3 * 4 + 5
(2 + 3) * (4 + 5)

## Division
618 / 10
618 // 10

618 % 10
from operator import truediv, floordiv, mod
floordiv(618, 10)
truediv(618, 10)
mod(618, 10)

## Approximation
5 / 3
5 // 3
5 % 3

## Multiple return values
def divide_exact(n, d):
    return n //d, n % d

quotient, remainder = divide_exact(2013, 10)
print("Quotient:", quotient)
print("Remainder:", remainder)

## Dostrings, doctests, & default arguments
def divide_exact(n ,d = 10):
    """Return the quotient and remainder of dividing N by D.

    >>> q, r = divide_exact(2013 ,10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n,d), mod(n, d)

## Conditional expressions
def absolute_value(x):
    """Return the absolute value of x.

    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    elif x ==0:
        return 0
    else:
        return x

# Boolean operators
not 0
not None

## Summation via while
i, total = 0, 0
while i < 3:
    i = i + 1
    total += i
total