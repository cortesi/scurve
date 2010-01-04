"""
    Some common test routines.
"""

def is_traversal(lst):
    """
        Does this list of points visit every vertex on the n-dimensional
        cube once, with each value differing from the previous value by
        exactly one bit?
    """
    lst = [tuple(i) for i in lst]
    assert len(lst) == len(set(lst))
    prev = None
    for i in lst:
        if prev is not None:
            diff = 0
            for x, y in zip(i, prev):
                if x != y:
                    if abs(x-y) != 1:
                        raise AssertionError("%s and %s differ by more than 1."%(i, prev))
                    diff += 1
            assert diff == 1
        prev = i

def symmetry(c):
    l1 = list(c)
    l2 = [c.index(i) for i in l1]
    assert l2 == range(len(c))




