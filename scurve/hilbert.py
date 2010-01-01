import utils, math


def transform(entry, direction, width, x):
    assert x < 2**width
    assert entry < 2**width
    return utils.rrot((x^entry), direction+1, width)


def itransform(entry, direction, width, x):
    """
        Inverse transform - we simply reverse the operations in transform.
    """
    assert x < 2**width
    assert entry < 2**width
    return utils.lrot(x, direction+1, width)^entry
    # There is an error in the Hamilton paper's formulation of the inverse
    # transform in Lemma 2.12. The correct restatement as a transform is as follows: 
    #return transform(rrot(entry, direction+1, width), width-direction-2, width, x)


def direction(x, n):
    assert x < 2**n
    if x == 0:
        return 0
    elif x%2 == 0:
        return utils.tsb(x-1, n)%n
    else:
        return utils.tsb(x, n)%n


def entry(x):
    if x == 0:
        return 0
    else:
        return utils.graycode(2*((x-1)/2))


def hilbert_point(dimension, order, h):
    """
        Convert an index on the Hilbert curve of the specified dimension and
        order to a set of point coordinates.
    """
    #    The bit widths in this function are:
    #        p[*]  - order
    #        h     - order*dimension
    #        l     - dimension
    #        e     - dimension
    h = utils.bits(h, order*dimension)
    e, d = 0, 0
    p = [0]*dimension
    for i in range(order):
        w = h[i*dimension:i*dimension+dimension]
        w = utils.bits2int(w)
        l = utils.graycode(w)
        l = itransform(e, d, dimension, l)
        l = utils.bits(l, dimension)
        for j in range(dimension):
            p[j] = utils.setbit(p[j], order, i, l[j])
        e = e ^ utils.lrot(entry(w), d+1, dimension)
        d = (d + direction(w, dimension) + 1)%dimension
    return p


def hilbert_index(dimension, order, p):
    # Hamilton's paper initialises d as 0, which I believe to be an error.
    h, e, d = 0, 0, 1
    p = [utils.bits(i, order) for i in p]
    for i in range(order):
        l = [p[x][i] for x in range(dimension)]
        l.reverse()
        l = utils.bits2int(l)
        l = transform(e, d, dimension, l)
        w = utils.igraycode(l)
        e = e ^ utils.lrot(entry(w), d+1, dimension)
        d = (d + direction(w, dimension) + 1)%dimension
        h = (h<<dimension)|w
    return h


class Hilbert:
    def __init__(self, dimension, order):
        self.dimension, self.order = dimension, order

    def index(self, p):
        return hilbert_index(self.dimension, self.order, p)

    def point(self, idx):
        return hilbert_point(self.dimension, self.order, idx)




