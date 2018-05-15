## Readings:
# http://composingprograms.com/pages/13-defining-new-functions.html
# http://composingprograms.com/pages/14-designing-functions.html

## Imports
from math import pi
pi * 71 / 223

from math import sin
sin(pi * 2)

## Assignment
# = symbol is called the assignment operator
radius = 10
radius
2 * radius

# assign multiple values to multiple names in a single statement
area, circ = pi * radius * radius, 2 * pi * radius
area
circ
area, circ

# Changing the value of one name does not affect other names
radius = 20
area, circ

# Updating the value of area requires another assignment statement.
area = pi * radius * radius
area

## Function values
max(1, 2, 3)
f = max
f(1, 2, 3)

# When a name is bound to a new value through assignment,
# it is no longer bound to any previous value.
max = 7
max
f(1, 2, max)

# But the max function is now broken, if you want to set it back
max = f
max
max(1, 6, 2)

## User-defined functions
def square(x):
    return mul(x, x)
square(21)
square(add(2, 5))
square(square(3))

def sum_squares(x, y):
    return add(square(x), square(y))
sum_squares(3, 4)
sum_squares(5, 12)

def area():
    return pi * radius * radius
area()
radius = 5
area()

## Discussion 1
f = min
f = max
g, h = min, max
max = g
max(f(2, g(h(1, 5), 3)), 4)
# The real expression is
max = f
min(max(2, min(max(1, 5), 3)), 4)

def square(square):
    return mul(square, square)
square
square(4)