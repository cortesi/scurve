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
    parser.add_option("-c", "--color", action="store", dest="color", default="0A2376")
    parser.add_option(
        "-b", "--background", action="store", dest="background", default="FFFFFF"
    )
    parser.add_option(
        "-s", "--size", action="store",
        type="int", dest="size", default=100
    )
    parser.add_option(
        "-o", "--order", action="store",
        type="int", dest="order", default=None,
        help = "Order of the curve."
    )
    parser.add_option(
        "-p", "--points", action="store",
        type="int", dest="points", default=None,
        help = "Total number of points on the curve."
    )
    parser.add_option(
        "-d", "--dotsize", action="store",
        type="int", dest="dotsize", default=2
    )
    parser.add_option(
        "-m", "--mark", action="append",
        type="int", dest="mark", default=[]
    )
    parser.add_option(
        "-u", "--curve", action="store",
        type="str", dest="curve", default="hilbert"
    )
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error("Please specify output file.")

    if options.order:
        c = scurve.fromOrder(options.curve, 2, options.order)
    elif options.points:
        c = scurve.fromSize(options.curve, 2, options.points)
    else:
        parser.error("Must specify either points or order.")

    d = draw.Demo(
            c,
            options.size,
            options.color,
            options.background,
            options.dotsize,
            *options.mark
        )
    d.draw()
    d.save(args[0])


main()
