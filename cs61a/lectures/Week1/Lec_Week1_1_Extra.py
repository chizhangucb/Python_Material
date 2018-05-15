#===== The Non-Pure Print Function =====#

-2
None  # a special Python value that represents nothing
print(None)
print(None, None)
print(1, 2, 3)

## 1. Pure function:
# Functions have some input (their arguments) and
# return some output (the result of applying them).
abs(-2)

# (1) Pure functions have the property that applying
# them has no effects beyond returning a value.
# (2) Moreover, a pure function must always return the
# same value when called twice with the same arguments.


## 2. Non-pure function:
# In addition to returning a value, applying a non-pure
# function can generate side effects, which:
# make some change to the state of the interpreter or computer
# eg. generate additional output beyond the return value

print(print(1), print(2))
# The value that print returns is always None

print(print(print(1, 2), print(3)),
      print(print(4), print(5)),
      print(7))

# A function that does NOT explicitly return a value will return None
# But, None is not displayed by the interpreter as the value of an exp
def does_not_square(x):
    x * x
does_not_square(4)
print(does_not_square(4))

sixteen = does_not_square(4)
sixteen
sixteen + 4