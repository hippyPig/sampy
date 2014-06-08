from math import sqrt
from functools import wraps



################################################################################
# Functions
################################################################################
def quad(*args):
    """Add in quadrature"""
    if not len(args): return 0
    if isinstance(args[0], list):
        return sqrt(sum(float(x)**2 for x in args[0]))
    return sqrt(sum(float(x)**2 for x in args))


def product(*args):
    """Make product of all arguments"""
    if not len(args): return 0
    if isinstance(args[0], list):
        return reduce(lambda x, y: x*y, args[0])
    return reduce(lambda x, y: x*y, args)


def depth(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += depth(item)
        return count + 1




################################################################################
if __name__ == "__main__":
    """TEST"""










