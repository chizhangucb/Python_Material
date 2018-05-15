## Functions as Abstractions
# A function definition should be able to suppress details.
# The users of the function may not have written the function themselves.


## Operators
# Division: Python provides two infix operators: / and //.
# / is normal division, returning a floating point, or decimal value
8 / 4
5 / 4
# // rounds the result down to an integer
8 // 4
5 // 4

# These two operators are shorthand for the truediv and floordiv functions
from operator import truediv, floordiv
truediv(5, 4)
floordiv(5, 4)

## Designing Functions
# Documentation
def pressure(v, t, n):
    """Compute the pressure in pascals of an ideal gas.

    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas
    """
    k = 1.38e-23  # Boltzmann's constant
    return n * k * t / v

help(pressure)