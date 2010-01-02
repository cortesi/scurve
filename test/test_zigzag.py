import libpry
from scurve import zigzag, utils


class uZigZag(libpry.AutoTree):
    def is_traversal(self, lst):
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

    def symmetry(self, c):
        l1 = list(c)
        l2 = [c.index(i) for i in l1]
        assert l2 == range(len(c))

    def test_point(self):
        self.is_traversal(zigzag.ZigZag(1, 1))
        self.is_traversal(zigzag.ZigZag(1, 3))
        self.is_traversal(zigzag.ZigZag(2, 3))
        self.is_traversal(zigzag.ZigZag(3, 3))
        self.is_traversal(zigzag.ZigZag(3, 12))
        self.is_traversal(zigzag.ZigZag(4, 3))
        self.is_traversal(zigzag.ZigZag(4, 4))

    def test_index(self):
        self.symmetry(zigzag.ZigZag(1, 1))
        self.symmetry(zigzag.ZigZag(2, 3))
        self.symmetry(zigzag.ZigZag(2, 4))
        self.symmetry(zigzag.ZigZag(3, 2))
        self.symmetry(zigzag.ZigZag(3, 12))
        self.symmetry(zigzag.ZigZag(4, 4))



tests = [
    uZigZag()
]
