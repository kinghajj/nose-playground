from functools import reduce

def factorial(n):
    """
    >>> factorial(5)
    120
    """
    return reduce(lambda x, y: x * y, xrange(1, n + 1))
