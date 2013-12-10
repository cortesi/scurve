from scurve import utils
import tutils

class TestFunctions:
    def test_bits2int(self):
        assert utils.bits2int([0, 0, 1]) == 1
        assert utils.bits2int([0, 1, 1]) == 3
        assert utils.bits2int([1, 1, 1]) == 7
        assert utils.bits2int([1, 0, 1]) == 5

    def test_graycode(self):
        assert utils.graycode(3) == 2
        assert utils.graycode(4) == 6

    def test_igraycode(self):
        for i in range(10):
            assert utils.igraycode(utils.graycode(i)) == i
            assert utils.graycode(utils.igraycode(i)) == i

    def rotpair(self, left, right, i, width):
        assert utils.rrot(left, i, width) == right
        assert utils.lrot(right, i, width) == left
        assert utils.lrot(left, i, width) == utils.rrot(left, width-i, width)

    def test_rot(self):
        self.rotpair(2, 1, 1, 2)
        self.rotpair(1, 2, 1, 2)
        self.rotpair(0, 0, 1, 2)
        self.rotpair(3, 3, 1, 2)
        self.rotpair(4, 2, 1, 3)
        self.rotpair(4, 1, 2, 3)
        self.rotpair(1, 2, 2, 3)
        self.rotpair(1, 1, 3, 3)

    def test_tsb(self):
        assert utils.tsb(1, 5) == 1
        assert utils.tsb(2, 5) == 0
        assert utils.tsb(3, 5) == 2
        assert utils.tsb((2**5)-1, 5) == 5
        assert utils.tsb(0, 5) == 0

    def test_setbit(self):
        assert utils.setbit(0, 3, 0, 1) == 4
        assert utils.setbit(4, 3, 2, 1) == 5
        assert utils.setbit(4, 3, 0, 0) == 0

    def test_bitrange(self):
        def checkbit(i, width, start, end, expected):
            e = utils.bitrange(i, width, start, end)
            assert e == expected
            assert e == utils.bits2int(utils.bits(i, width)[start:end])

        checkbit(1, 5, 4, 5, 1)
        checkbit(2, 5, 4, 5, 0)
        checkbit(2, 5, 3, 5, 2)
        checkbit(2, 5, 3, 4, 1)
        checkbit(3, 5, 3, 5, 3)
        checkbit(3, 5, 0, 5, 3)
        checkbit(4, 5, 2, 3, 1)
        checkbit(4, 5, 2, 4, 2)
        checkbit(4, 5, 2, 2, 0)

    def test_entropy(self):
        tutils.raises(ValueError, utils.entropy, "foo", 64, 0)
        assert utils.entropy("a"*64, 64, 1) == 0
        d = "".join([chr(i) for i in range(256)])
        assert utils.entropy(d, 64, 1) == 1

