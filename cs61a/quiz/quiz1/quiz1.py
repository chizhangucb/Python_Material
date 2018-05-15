# CS 61A Fall 2014
# Name:
# Login:


def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the
    third is not.

    >>> two_equal(1, 2, 3)
    False
    >>> two_equal(1, 2, 1)
    True
    >>> two_equal(1, 1, 1)
    False
    >>> result = two_equal(5, -1, -1) # return, don't print
    >>> result
    True

    """
    if a == b and b == c and a == c:
        return False
    elif a != b and a != c and b != c:
        return False
    else:
        return True


def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    a1 = a2 = a; b1 = b2 =b
    while a1 > 1 and a1 != b1:
        if (a1 % 2 == 0):
            a1 = a1 / 2
        else:
            a1 = a1 * 3 + 1
    while b2 > 1 and b2 != a2:
        if (b2 % 2 == 0):
            b2 = b2 / 2
        else:
            b2 = b2 * 3 + 1
    if a1 != b1 and a2 != b2:
        return False
    else:
        return True


def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19

    """
    semi = perimeter / 2
    h0, a, w0 = 1.0, 2.0, semi - 1.0
    diff0 = abs(h0/w0 - w0/h0 + 1)
    while a < semi:
        h1, w1 = a, semi - a
        diff1 = abs(h1/w1 - w1/h1 + 1)
        if diff1 < diff0:
            h0, w0 = h1, w1
            diff0 = diff1
        a = a + 1
    return int(h0)
