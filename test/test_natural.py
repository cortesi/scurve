from scurve import natural, utils
import tutils


class TestNatural:
    def test_point(self):
        tutils.is_complete(natural.Natural(1, 1))
        tutils.is_complete(natural.Natural(1, 3))
        tutils.is_complete(natural.Natural(2, 3))
        tutils.is_complete(natural.Natural(3, 3))
        tutils.is_complete(natural.Natural(3, 12))
        tutils.is_complete(natural.Natural(4, 3))
        tutils.is_complete(natural.Natural(4, 4))

    def test_index(self):
        tutils.symmetry(natural.Natural(1, 1))
        tutils.symmetry(natural.Natural(2, 3))
        tutils.symmetry(natural.Natural(2, 4))
        tutils.symmetry(natural.Natural(3, 2))
        tutils.symmetry(natural.Natural(3, 12))
        tutils.symmetry(natural.Natural(4, 4))

    def test_fromSize(self):
        z = natural.Natural(2, 3)
        z2 = natural.Natural.fromSize(2, len(z))
        assert z.dimension == z2.dimension
        assert z.size == z2.size

        z = natural.Natural(3, 256)
        z2 = natural.Natural.fromSize(3, len(z))
        assert z.dimension == z2.dimension
        assert z.size == z2.size


