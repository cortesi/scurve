from scurve import hcurve


class TestHcurve:
    def test_xycor(self):
        n = 4
        h = hcurve.Hcurve(2, n)
        for i in range(n*n):
            assert h.xcor(i, n) < n
            assert h.ycor(i, n) < n

    def test_fromSize(self):
        h = hcurve.Hcurve.fromSize(2, 16)
        assert h.size == 4
        assert len(h) == 16

    def test_traversal(self):
        h = hcurve.Hcurve.fromSize(2, 16)
        assert [i for i in h]
