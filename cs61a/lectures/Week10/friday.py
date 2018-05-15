# Python raises an exception whenever an erro occurs/
# Exceptions can be handled by the program, preventing the interpreter from halting
# Exceptions are objects! They have classes with constructors.
# They enable non-local continuations of control.

# 1. Assetions are designed to be used libearally. They can be ignored to increase efficiency by
# python3 -O   (big O)
# Whether assertions are enabled is governed by a bool __debug__
__debug__   # True
# After using python -O , __debug__ becomes false.

def assert_false():
    assert False, 'False!'

# 2. Raise statement.  raise <expression>
# <expression> must evaluate to a subclass of BaseException or an instance of one.
# Exceptions are constructed like any other object. 
# a. TypeError -- A function was passed the wrong number/type of argument
# b. NameError -- A name wasn't found
# c. KeyError -- A key wasn't found in a dictionary
# d. RuntimeError -- Catch-all for troubles during interpretation

raise TypeError('Bad argument')
abs('hello')  # TypeError
hello         # NameError
{}['hello']   # KeyError
def f(): f()  # RuntimeError  

# 3. Try statements: handle exceptions
# try:
#     <try suite>
# except <exception class> as <name>
#     <except suite>
# Execution rule: The <try suite> is executed first.
# If, during the course of executing the <try suite>, an exception is raised thatis not handled otherwise,
# and if the class of the exception inherits from <exception class>, then
# The <except suite> is executed, with <name> bound to the exception.
try:
    x = 1/0
except ZeroDivisionError as e:
    print('handling a', type(e))
    x = 0

# handling a <class 'ZeroDivisionError'>


def invert(x):
    """Return 1/x

    >>> invert(2)
    Never printed if x is 0
    0.5
    """
    result = 1/x  # Raises a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return result

def invert_safe(x):
    """Return 1/x, or the string 'divison by zero' if x is 0.

    >>> invert_safe(2)
    Never printed if x is 0
    0.5
    >>> invert_safe(0)
    'division by zero'
    """
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)

try:
    invert_safe(0)
except ZeroDivisionError as e:
    print("handled")

# invert_safe(1/0)  => Errror, not be handled
