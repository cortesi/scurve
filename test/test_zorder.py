from scurve import zorder, utils
import tutils


class TestZOrder:
    def test_dimensions(self):
        z = zorder.ZOrder(2, 2)
        assert z.dimensions()[0] == (2**2)

    def test_point(self):
        z = zorder.ZOrder(2, 2)
        assert z.point(utils.bits2int([0, 1, 0, 1])) == [3, 0]
        assert z.point(utils.bits2int([0, 0, 0, 0])) == [0, 0]
        assert z.point(utils.bits2int([1, 0, 0, 0])) == [0, 2]
        assert z.point(utils.bits2int([1, 0, 1, 0])) == [0, 3]
        assert z.point(utils.bits2int([1, 1, 1, 1])) == [3, 3]

        z = zorder.ZOrder(2, 3)
        assert z.point(utils.bits2int([1, 1, 1, 1, 1, 1])) == [7, 7]

    def test_index(self):
        z = zorder.ZOrder(2, 3)
        tutils.symmetry(zorder.ZOrder(1, 1))
        tutils.symmetry(zorder.ZOrder(2, 3))
        tutils.symmetry(zorder.ZOrder(2, 4))
        tutils.symmetry(zorder.ZOrder(3, 2))
        tutils.symmetry(zorder.ZOrder(4, 3))

    def test_fromSize(self):
        z = zorder.ZOrder(2, 3)
        z2 = zorder.ZOrder.fromSize(2, len(z))
        assert z.dimension == z2.dimension
        assert z.bits == z2.bits

