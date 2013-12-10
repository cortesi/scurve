import math
from scurve import hilbert, utils
import tutils


class TestFunctions:
    def ispow2(self, i):
        """
            Is i a power of two?
        """
        l = math.log(i, 2)
        return l == int(l)
    
    def is_hilbertcube(self, lst):
        """
            Does this list visit every vertex on the n-dimensional unit cube
            once, with each value differing from the previous value by exactly
            one bit?
        """
        lst = lst[:]
        assert len(lst) == len(set(lst))
        assert self.ispow2(len(lst))
        # We also want to test that start and end positions are adjacent
        lst.append(lst[0])
        prev = 0
        for i in lst:
            if prev > 0:
                assert self.ispow2(prev^i)
            prev = i

    def transform_pair(self, a, entry, direction, width):
        r = transform(entry, direction, width, a)
        assert a == itransform(entry, direction, width, r)
    
    def test_transform(self):
        for width in range(2, 5):
            g = [utils.graycode(i) for i in range(2**width)]
            # Sanity: the gray sequence should be a Hilbert cube too
            self.is_hilbertcube(g)

            for e in range(2**width):
                for d in range(width):
                    x = [hilbert.transform(e, d, width, i) for i in g]

                    # From Lemma 2.11 of Hamilton
                    assert hilbert.transform(e, d, width, e) == 0
                    assert hilbert.itransform(e, d, width, 0) == e

                    # The base gray code starts at 0, and has a direction of width-1:
                    if e == 0 and d == width-1:
                        assert x == g
                    self.is_hilbertcube(x)
                    assert [hilbert.itransform(e, d, width, i) for i in x] == g

        # These values are from the example on p 18 of Hamilton
        assert hilbert.transform(0, 1, 2, 3) == 3
        assert hilbert.transform(3, 0, 2, 2) == 2
        assert hilbert.transform(3, 0, 2, 1) == 1

    def test_hilbert_point(self):
        for n in [2, 3, 4]:
            m = 3
            for i in range(2**(n*m)):
                v = hilbert.hilbert_point(n, m, i)
                assert i == hilbert.hilbert_index(n, m, v)

    def test_hilbert_index(self):
        # From the example on p 18 of Hamilton
        assert hilbert.hilbert_index(2, 3, [5, 6]) == 45

    def test_direction(self):
        assert hilbert.direction(2, 2) == 1
        assert hilbert.direction(3, 2) == 0
        assert hilbert.direction(1, 2) == 1

    def test_entry(self):
        assert hilbert.entry(2) == 0
        assert hilbert.entry(3) == 3
        assert hilbert.entry(1) == 0


class TestHilbert:
    def test_index(self):
        h = hilbert.Hilbert(2, 3)
        assert h.index(h.point(4)) ==  4

    def test_len(self):
        assert len(hilbert.Hilbert(2, 1)) == 4
        assert len(hilbert.Hilbert(2, 2)) == 16
        assert len(hilbert.Hilbert(3, 1)) == 8

    def test_getitem(self):
        assert len(list(hilbert.Hilbert(2, 1))) == 4

    def test_fromSize(self):
        h = hilbert.Hilbert.fromSize(2, 256*256)
        assert h.dimensions() == [256, 256]
        h = hilbert.Hilbert(3, 1)
        h2 = hilbert.Hilbert.fromSize(3, len(h))
        assert h.dimension == h2.dimension
        assert h.order == h2.order
        tutils.raises(ValueError, hilbert.Hilbert.fromSize, 3, 3)

    def ttest_bench(self):
        h = hilbert.Hilbert(2, 7)
        for i in h:
            h.index(i)


