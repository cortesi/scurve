#!/usr/bin/env python
import os.path, math
import scurve
from scurve import progress
import Image, ImageDraw


def drawmap(map, csource, name, quiet):
    c = Image.new("RGB", map.dimensions())
    cd = ImageDraw.Draw(c)
    step = len(csource)/float(len(map))
    if quiet:
        prog = progress.Dummy()
    else:
        prog = progress.Progress(len(map))
    for i, p in enumerate(map):
        color = csource.point(int(i*step))
        cd.point(tuple(p), fill=tuple(color))
        if not i%100:
            prog.tick(i)
    c.save(name)


def main():
    from optparse import OptionParser, OptionGroup
    parser = OptionParser(
                usage = "%prog [options] output",
                version="%prog 0.1",
            )
    parser.add_option(
        "-c", "--colorsource", action="store",
        type="str", dest="colorsource", default="hilbert"
    )
    parser.add_option(
        "-m", "--map", action="store",
        type="str", dest="map", default="hilbert"
    )
    parser.add_option(
        "-s", "--size", action="store",
        type="int", dest="size", default=512
    )
    parser.add_option(
        "-q", "--quiet", action="store_true",
        dest="quiet", default=False
    )
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error("Please specify output file.")

    csource = scurve.fromSize(options.colorsource, 3, 256**3)
    map = scurve.fromSize(options.map, 2, options.size**2)
    drawmap(map, csource, args[0], options.quiet)

main()

