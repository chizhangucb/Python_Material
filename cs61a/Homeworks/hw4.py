# CS 61A Fall 2014
# Name: Chi Zhang
# Login:

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

# Q1

def interval(a, b):
    """Construct an interval from a to b."""
    return [min(a, b), max(a, b)]

def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]

# Q2

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    assert lower_bound(y) > 0 or upper_bound(y) < 0
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q3

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)

def sub_interval_alt(x, y):
    negative_y = interval(-upper_bound(y), -lower_bound(y))
    return add_interval(x, negative_y)

# Q4

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# These two intervals give different results for parallel resistors:
range1 = (1, 2)
range2 = (4, 6)
print(str_interval(par1(range1, range2)), "!=", par2(range1, range2))

# Q5

def multiple_references_explanation():
    return """The mulitple reference problem exists in Alyssa's system if we choose par1. The true value within an interval is fixed but unknow.
           If the same interval is referred twice within a function, it may select two different true values from the interval, which is an error
           that results in intervals that are larger than they should be. It happens in par1 function
           For example, if the true value is within the interval (-1, 1), and we have two methods to calculate the square of the true value. First,
           a * a can be used. Normally, the result won't be negative. However, if we firstly select -1 and secondly 1, tbe result will be -1, which
           is wrong! Second, we can use pow(a, 2), which is better than the first method."""

# Q6

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    def f(t):
        return a*t*t + b*t + c
    extreme = - b / (2 * a)
    if lower_bound(x) <= extreme <= upper_bound(x):
        lower = min(f(lower_bound(x)), f(upper_bound(x)), f(extreme))
        upper = max(f(lower_bound(x)), f(upper_bound(x)), f(extreme))
        return interval(lower, upper)
    else:
        lower = min(f(lower_bound(x)), f(upper_bound(x)))
        upper = max(f(lower_bound(x)), f(upper_bound(x)))
        return interval(lower, upper)

def quadratic_alt(x, a, b, c):
    f = lambda t: a*t*t + b*t + c
    extreme = - b / (2 * a)
    lower, upper, extreme= map(f, (lower_bound(x), upper_bound(x), extreme))
    if lower_bound(x) <= extreme <= upper_bound(x):
        return interval(min(lower, upper, extreme), max(lower, upper, extreme))
    else:
        return interval(min(lower, upper), max(lower, upper))

# Q7

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.
    >>> str_interval(polynomial(interval(0, 2), (-1, 3, -2)))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), (1, -3, 2)))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), (10, 24, -6, -8, 3)))
    '18.0 to 23.0'
    """
    # Original function
    def next_fn(coeff, k, f):
        return lambda x: coeff * pow(x, k) + f(x)

    # First derivative
    def next_dfn(coeff, k, df):
        return lambda x: k * coeff * pow(x, k-1) + df(x)

    # Second derivative
    def next_ddfn(coeff, k, ddf):
        return lambda x: k * (k-1) * coeff * pow(x, k-2) + ddf(x)

    f = lambda x: 0
    df = lambda x: 0
    ddf = lambda x: 0
    for k, coeff in enumerate(c):
        f = next_fn(coeff, k, f)
        if k > 0:
            df = next_dfn(coeff, k, df)
        if k > 1:
            ddf = next_ddfn(coeff, k, ddf)

    # Find extreme points
    lower, upper = lower_bound(x), upper_bound(x)
    num_steps = 30
    step = (upper - lower) / num_steps
    starts = tuple(lower + k * step for k in range(num_steps))
    extreme = tuple(find_zero(df, ddf, n) for n in starts)

    # Filter for the interval x and return
    candidates = tuple(n for n in extreme if n > lower and n < upper) + (lower, upper)
    values = [f(n) for n in candidates]
    return interval(min(values), max(values))


# Newton's method from Week3 Friday Lecture

def improve(update, close, guess=1, max_updates=100):
    """Iteratively improve guess with update until close(guess) is true or
    max_updates have been applied."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def find_zero(f, df, guess=1):
    """Return a zero of the function f with derivative df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero, guess)

def newton_update(f, df):
    """Return an update function for f with derivative df,
    using Newton's method."""
    def update(x):
        return x - f(x) / df(x)
    return update



