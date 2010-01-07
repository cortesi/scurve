#!/usr/bin/env python
import os.path, math
import scurve
from scurve import progress
import Image, ImageDraw

def sortedPixels(csource, img, quiet):
    img = Image.open(img, "r")
    decorated = []
    if quiet:
        prog = progress.Dummy()
    else:
        prog = progress.Progress(
            img.size[0]*img.size[1],
            "Analysing image"
        )
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            p = img.getpixel((x, y))
            decorated.append(
                (csource.index(p), p)
            )
            if not x*y%100:
                prog.tick(x*y)
    decorated.sort()
    return [i[1] for i in decorated]


def drawmap(map, pixels, name, quiet):
    c = Image.new("RGB", map.dimensions())
    cd = ImageDraw.Draw(c)
    step = len(pixels)/float(len(map))
    if quiet:
        prog = progress.Dummy()
    else:
        prog = progress.Progress(len(map), "Creating swatch")
    for i, p in enumerate(map):
        color = pixels[int(i*step)]
        cd.point(tuple(p), fill=tuple(color))
        if not i%100:
            prog.tick(i)
    c.save(name)


def main():
    from optparse import OptionParser, OptionGroup
    parser = OptionParser(
                usage = "%prog [options] image_path output_path",
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
        type="int", dest="size", default=256
    )
    parser.add_option(
        "-q", "--quiet", action="store_true",
        dest="quiet", default=False
    )
    options, args = parser.parse_args()
    if len(args) != 2:
        parser.error("Please specify output file.")

    csource = scurve.fromSize(options.colorsource, 3, 256**3)
    map = scurve.fromSize(options.map, 2, options.size**2)
    p = sortedPixels(csource, args[0], options.quiet)
    drawmap(map, p, args[1], options.quiet)
    


main()

