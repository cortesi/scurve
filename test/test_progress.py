import scurve.progress as progress
import StringIO

class TestInplace:
    def test_basic(self):
        s = StringIO.StringIO()
        c = progress.Inplace(stream=s)
        assert s.getvalue() ==  ''
        c.tick(10)
        assert s.getvalue() ==  '\r10'
        c.tick(10000)
        assert s.getvalue() ==  '\r10\r10000'
        c.inject("foo")
        c.clear()

    def test_nostream(self):
        c = progress.Inplace(stream=None)
        c.tick(10)
        c.clear()


class TestProgress:
    def test_basic(self):
        s = StringIO.StringIO()
        p = progress.Progress(100, stream=s)
        p.tick(25)
        assert p.prev == 0.25
        p.tick(50)
        assert p.prev == 0.5
        p.full()
        assert p.prev == 1.0
