"""
    Some common test routines.
"""

def raises(exc, obj, *args, **kwargs):
    """
        Assert that a callable raises a specified exception.

        :exc An exception class or a string. If a class, assert that an
        exception of this type is raised. If a string, assert that the string
        occurs in the string representation of the exception, based on a
        case-insenstivie match.

        :obj A callable object.

        :args Arguments to be passsed to the callable.

        :kwargs Arguments to be passed to the callable.
    """
    try:
        apply(obj, args, kwargs)
    except Exception, v:
        if isinstance(exc, basestring):
            if exc.lower() in str(v).lower():
                return
            else:
                raise AssertionError(
                    "Expected %s, but caught %s"%(
                        repr(str(exc)), v
                    )
                )
        else:
            if isinstance(v, exc):
                return
            else:
                raise AssertionError(
                    "Expected %s, but caught %s %s"%(
                        exc.__name__, v.__class__.__name__, str(v)
                    )
                )
    raise AssertionError("No exception raised.")


def is_complete(lst):
    """
        Does this list of points visit every vertex on the n-dimensional
        cube once?
    """
    lst = [tuple(i) for i in lst]
    assert len(lst) == len(set(lst))


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




