import math
import cairo

class Canvas:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

    def ctx(self):
        return cairo.Context(self.surface)

    def background(self, r, g, b, a):
        c = self.ctx()
        c.set_source_rgba(r, g, b, a)
        c.rectangle(0, 0, self.width, self.height)
        c.fill()
        c.stroke()

    def save(self, fname):
        self.surface.write_to_png(fname)


def parseColor(c):
    """
        Parse an HTML-style color specification
    """ 
    if len(c) == 6:
        r = int(c[0:2], 16)/255.0
        g = int(c[2:4], 16)/255.0
        b = int(c[4:6], 16)/255.0
        return [r, g, b]
    elif len(c) == 3:
        return c


class Demo:
    """
        Draws a 2d curve within a specified square.
    """
    PAD = 5
    def __init__(self, curve, size, color, dotsize, *marks):
        self.curve = curve
        self.size, self.color, self.dotsize = size, color, dotsize
        self.c = Canvas(size+self.PAD*2, size+self.PAD*2)
        self.c.background(1, 1, 1, 1)
        self.ctx = self.c.ctx()
        self.ctx.set_line_width(1)
        # Assuming all dimension sizes are equal
        self.length = self.curve.dimensions()[0]
        self.marks = set(marks)
        self.scale = float(size)/(math.sqrt(self.length)-1)

    def func(self, i, o):
        return xy(i, o)

    def _coordinates(self):
        for x, y in self.curve:
            x *= self.scale
            y *= self.scale
            assert x <= self.size
            assert y <= self.size
            yield x+self.PAD, y+self.PAD

    def draw(self):
        self.ctx.move_to(self.PAD, self.PAD)
        off = 0
        lst = list(self._coordinates())
        for x, y in lst:
            if off in self.marks:
                self.ctx.set_source_rgba(1, 0, 0, 0.8)
                self.ctx.arc(x, y, self.dotsize*2, 0, math.pi*2)
                self.ctx.fill()
            else:
                self.ctx.set_source_rgba(1, 0, 0, 0.5)
                self.ctx.arc(x, y, self.dotsize, 0, math.pi*2)
                self.ctx.fill()
            off += 1

        self.ctx.set_source_rgb(*parseColor(self.color))
        self.ctx.move_to(self.PAD, self.PAD)
        for x, y in lst:
            self.ctx.line_to(x, y)
        self.ctx.stroke()

    def save(self, fname):
        self.c.save(fname)

