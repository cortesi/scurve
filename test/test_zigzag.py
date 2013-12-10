from scurve import zigzag, utils
import tutils


class TestZigZag:
    def test_point(self):
        tutils.is_traversal(zigzag.ZigZag(1, 1))
        tutils.is_traversal(zigzag.ZigZag(1, 3))
        tutils.is_traversal(zigzag.ZigZag(2, 3))
        tutils.is_traversal(zigzag.ZigZag(3, 3))
        tutils.is_traversal(zigzag.ZigZag(3, 12))
        tutils.is_traversal(zigzag.ZigZag(4, 3))
        tutils.is_traversal(zigzag.ZigZag(4, 4))

    def test_index(self):
        tutils.symmetry(zigzag.ZigZag(1, 1))
        tutils.symmetry(zigzag.ZigZag(2, 3))
        tutils.symmetry(zigzag.ZigZag(2, 4))
        tutils.symmetry(zigzag.ZigZag(3, 2))
        tutils.symmetry(zigzag.ZigZag(3, 12))
        tutils.symmetry(zigzag.ZigZag(4, 4))

    def test_fromSize(self):
        z = zigzag.ZigZag(2, 3)
        z2 = zigzag.ZigZag.fromSize(2, len(z))
        assert z.dimension == z2.dimension
        assert z.size == z2.size

        z = zigzag.ZigZag(3, 256)
        z2 = zigzag.ZigZag.fromSize(3, len(z))
        assert z.dimension == z2.dimension
        assert z.size == z2.size

