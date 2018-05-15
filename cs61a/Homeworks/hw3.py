# CS 61A Fall 2014
# Name: Chi Zhang
# Login:

# Q1
def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    final, k, gn_1, gn_2, gn_3 = 0, 3, 3, 2, 1
    if n <= 3:
        final = n
        return final
    else:
        while k < n:
            final = gn_1 + 2 * gn_2 + 3 * gn_3
            gn_1, gn_2, gn_3 = final, gn_1, gn_2
            k += 1
        return final

# Q2
def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k < 10:
        return k == 7
    else:
        return has_seven(k // 10) or has_seven(k % 10)

# Q3
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    def pingpong_move(k, h, up):
        if k % 7 == 0 or has_seven(k):
            return pingpong_forward(k, h, not up)
        else:
            return pingpong_forward(k, h, up)
        
    def pingpong_forward(k, h, up):
        if k == n:
            return h
        if up:
            return pingpong_move(k+1, h+1, up)
        else:
            return pingpong_move(k+1, h-1, up)

    return pingpong_forward(1, 1, True)

def pingpong_iter(n):
    """Return the nth element of the ping-pong sequence by iteration.

    >>> pingpong_iter(7)
    7
    >>> pingpong_iter(8)
    6
    >>> pingpong_iter(15)
    1
    >>> pingpong_iter(21)
    -1
    >>> pingpong_iter(22)
    0
    >>> pingpong_iter(30)
    6
    >>> pingpong_iter(68)
    2
    >>> pingpong_iter(69)
    1
    >>> pingpong_iter(70)
    0
    >>> pingpong_iter(71)
    1
    >>> pingpong_iter(72)
    0
    >>> pingpong_iter(100)
    2
    """
    h, k, direction = 1, 1, 1
    while k < n:
        if k % 7 ==0 or has_seven(k):
            direction = - direction
        h = h + direction
        k = k + 1
    return h

# Q4
def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_partitions(m, n):
        if m < 0:
            return 0
        elif m == 0:
            return 1
        elif n > m:
            return 0
        else:
            with_m = count_partitions(m - n, n)
            without_m = count_partitions(m, n * 2)
            return with_m + without_m
    return count_partitions(amount, 1)
        
# Q5
def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print("Move the top disk from rod", start , "to rod", end)
    else:
        towers_of_hanoi(n-1, start, 6 - start - end)
        print("Move the top disk from rod", start , "to rod", end)
        towers_of_hanoi(n-1, 6 - start - end, end)
    
# Q6

from operator import sub, mul

fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
fact(5)  # 120

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return (lambda f: lambda k: f(f, k))(lambda f, k: 1 if k == 1
                                        else mul(k, f(f, sub(k, 1))))
