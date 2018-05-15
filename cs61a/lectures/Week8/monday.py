# Lecture 18 

# String representations
# The str is legible to humans
# The repr is legible to the Python interpreter
# The str and repr strings are often the same, but not always.

# The repr String for an object
# The repr function returns a python expression (a string) that evaluates to an equal object.
# For most object types, eval(repr(object)) == object.
# The result of calling repr on a value is what Python prints in an interactive session

12e12               # 12000000000000.0
print(repr(12e12))  # '12000000000000.0'
repr(min)           # '<built-in function min>'

# The str String for an object
# The reuslt of calling str on the value of an expression is what Python prints using the print function.

def str_repr_demos():
    from datetime import date
    today = date(2014, 10, 13)
    today                 # datetime.date(2014, 10, 13)
    repr(today)           # 'datetime.date(2014, 10, 13)'
    print(today)

    s = 'hello world'
    str(s)                # 'Hello world'
    repr(s)               # "'Hello world'"
    "'hello world'"
    eval(repr(s))         # 'Hello world'
    repr(repr(s))         # '"\'Hello world\'"'
    repr(repr(repr(s)))   # '\'"\\\'Hello world\\\'"\''
    eval(eval(eval(repr(repr(repr(s))))))
    # Errors: eval('hello world')
    
# Polymorphic function: a function that applies to many different forms of data
# str and repr are both polymorphic; they apply to any object
# repr invokes a zero-argument method __repr__ on its argument
# str invokes a zero-argument method __str__ on its argument
today.__repr__()      # 'datetime.date(2014, 10, 13)'
today.__str__()       # '2014-10-13'

class Bear:
    def __init__(self):
        self.__repr__ = lambda: "oski"
        self.__str__ = lambda: "this bear instance"
        
    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear'

# The behavior of repr is complicated than invoking __repr__ on its argument
# => An instance attribute called __repr__ is ignored; Only class attributes are found.
# The behavior of str is also complicated:
# 1. An instance attribute called __str__ is ignored.
# 2. If no __str__ attribute is found, use repr string

def print_bear():
    oski = Bear()
    print(oski)             # a bear
    print(str(oski))        # a bear
    print(repr(oski))       # Bear()
    print(oski.__repr__())  # oski
    print(oski.__str__())   # this bear instance

def repr(x):
    type(x).__repr__(x)

def str(x):
    t = type(x)
    if hasattr(t, "__str__"):
        return t.__str__(x)
    else:
        return repr(x)

# Interface
# Message passing: objects interact by looking up attributes on each other (passing message)
# The attribute look-up rules allow different data type to repsond to the same message
# A shared message (attribute name) that elicits similar behavior from different object classes is a powerful method of abstraction

# Property Methods
# Often, we want the value of instance attributes to stay in sync.
# @property allows zero-argument methods to be callde without an explicit call expression.

class Rational:
    """A mutable fraction.

    >>> f = Rational(3, 5)
    >>> f
    Rational(3, 5)
    >>> print(f)
    3/5
    >>> f.float_value
    0.6
    >>> f.numer = 4
    >>> f.float_value
    0.8
    >>> f.denom -= 3
    >>> f.float_value
    2.0
    """
    
    def __init__(self, n, denom):
        self.numer = n
        self.denom = denom

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    @property
    def float_value(self):
        return self.numer / self.denom

# Implementing Complex Arithmetic
# Rectangular or Polar representation: perform arithmetic using the most convenient way
 
# An Interface for Complex Numbers.
# 1. All complex numbers should have real and imag components.
# 2. All complex numbers should have a magnitude and angle.
# 3. All complex numbers should share an implementation of add and mul

from math import atan2, sin, cos, pi

class Complex:
    def add(self, other):
        return ComplexRI(self.real + other.real,
                         self.imag + other.imag)
    def mul(self, other):
        return complexMA(self.magnitude * other.magnitude,
                         self.angle + other.angle)

class ComplexRI(Complex):
    """A rectangular representation of a complex number.

    >>> from math import pi
    >>> ComplexRI(1, 2).add(ComplexMA(2, pi/2))
    ComplexRI(1.0000000000000002, 4.0)
    >>> ComplexRI(0, 1).mul(ComplexRI(0, 1))
    ComplexMA(1.0, 3.141592653589793)
    >>> ComplexRI(1, 2) + ComplexMA(2, 0)
    ComplexRI(3.0, 2.0)
    >>> ComplexRI(0, 1) * ComplexRI(0, 1)
    ComplexMA(1.0, 3.141592653589793)
    """

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return "ComplexRI({0}, {1})".format(self.real, self.imag)

class ComplexMA(Complex):
    """A polar representation of a complex number."""

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
        
    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return "ComplexMA({0}, {1})".format(self.magnitude, self.angle)
