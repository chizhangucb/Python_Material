from operator import add, sub

############# Q1. A Plus Abs B
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

############# Q2. Two of Three
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    # return a * a + b * b + c * c - pow(min(a, b, c), 2)
    # return max(a * a + b * b, b * b + c * c, a * a + c * c)
    return pow(sorted((a, b, c))[1], 2) + pow(sorted((a, b, c))[2], 2)

############# Q3. Largest Factor
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    factorList = []
    for i in range(1, n):
        if n % i == 0:
            factorList.append(i)
    return max(factorList)

############# Alternative
# def largest_factor(n):
#     factor =  n - 1
#     while factor > 0:
#         if n % factor == 0:
#             return factor
#         factor -= 1


############# Q4. If Function vs Statement
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True

def t():
    return 1

def f():
    Error

# with_if_function()
# it uses a call expression, which guarantees that all of its operand subexpressions
# will be evaluated before if_function is applied to the resulting arguments.
# Therefore, even if c returns True, the function f will be called

# with_if_statement()
# never call f if c returns True


############# Q5. Hailstone
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    hailstoneList = [n]
    print(n)
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)
        hailstoneList.append(n)
    return len(hailstoneList)