#!/usr/bin/env python
import os.path, math
import scurve
from scurve import draw

def main():
    from optparse import OptionParser, OptionGroup
    parser = OptionParser(
                usage = "%prog [options] output",
                version="%prog 0.1",
            )
    parser.add_option(
        "-s", "--height", action="store",
        type = "int", dest="height", default=50,
        help = "Height of the swatch."
    )
    parser.add_option(
        "-w", "--colorwidth", action="store",
        type = "int", dest="colorwidth", default=10,
        help = "Width of each color."
    )
    parser.add_option(
        "-p", "--points", action="store",
        type="int", dest="points", default=64,
        help = "Total number of points on the curve."
    )
    parser.add_option(
        "-c", "--curve", action="store",
        type="str", dest="curve", default="hilbert"
    )
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error("Please specify output file.")

    c = scurve.fromSize(options.curve, 3, options.points)

    d = draw.Swatch(c, options.colorwidth, options.height)
    d.save(args[0])


main()
