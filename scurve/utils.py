"""
    A lot of these functions are written for clarity rather than speed. We'll
    fix that in time.
"""
import math

def graycode(x):
    return x^(x>>1)


def igraycode(x):
    """
        Inverse gray code.
    """
    if x == 0:
        return x
    m = int(math.ceil(math.log(x, 2)))+1
    i, j = x, 1
    while j < m:
        i = i ^ (x>>j)
        j += 1
    return i


def bits(n, width):
    """
        Convert n to a list of bits of length width.
    """
    assert n < 2**width
    bin = []
    for i in range(width):
        bin.insert(0, 1 if n&(1<<i) else 0)
    return bin


def bits2int(bits):
    """
        Convert a list of bits to an integer.
    """
    n = 0
    for p, i in enumerate(reversed(bits)):
        n += i*2**p
    return n


def rrot(x, i, width):
    """
        Right bit-rotation.

        width: the bit width of x.
    """
    assert x < 2**width
    i = i%width
    x = (x>>i) | (x<<width-i)
    return x&(2**width-1)


def lrot(x, i, width):
    """
        Left bit-rotation.

        width: the bit width of x.
    """
    assert x < 2**width
    i = i%width
    x = (x<<i) | (x>>width-i)
    return x&(2**width-1)


def tsb(x, width):
    """
        Trailing set bits.
    """
    assert x < 2**width
    i = 0
    while x&1 and i <= width:
        x = x >> 1
        i += 1
    return i


def setbit(x, w, i, b):
    """
        Sets bit i in an integer x of width w to b.
        b must be 1 or 0
    """
    assert b in [1, 0]
    assert i < w
    if b:
        return x | 2**(w-i-1)
    else:
        return x & ~2**(w-i-1)


def bitrange(x, width, start, end):
    """
        Extract a bit range as an integer.
        (start, end) is inclusive lower bound, exclusive upper bound.
    """
    return x >> (width-end) & ((2**(end-start))-1)




